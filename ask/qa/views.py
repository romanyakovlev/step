from django.shortcuts import render, get_object_or_404
from qa.models import Question, Answer
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from qa.forms import AskForm, AnswerForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.sessions.models import Session
from datetime import datetime, timedelta

# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)

def any_questions(request,questions): # common view for new and popular
    limit=request.GET.get('limit',10)
    try:
        page=int(request.GET.get('page',1))
    except:
        raise Http404
    paginator=Paginator(questions,limit)
    paginator.baseurl='/?page='
    try:
        page=paginator.page(page)
    except:
        raise Http404
    return render(request, 'qa/new_questions.html', {
        'questions': page.object_list,
        'paginator':paginator, 'page':page,
	'user':request.user,
    })

new_questions=lambda request:any_questions(request, Question.objects.new().all()) # for new

pop_questions=lambda request:any_questions(request, Question.objects.popular().all()) # for popular

def question_detail(request, pk):
    try:
        question=Question.objects.get(pk=pk)
    except:
        raise Http404
    answers=Answer.objects.filter(question=question)

    #   AnswerForm creation
    form=AnswerForm(initial={'question':pk})

    return render(request, 'qa/question_detail.html',{
    'question':question,
    'answers':answers,
    'form':form,
    })

def form_ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user=request.user
            ask=form.save()
            url='/question/'+str(ask.pk)
            return HttpResponseRedirect(url)
    else:
        form=AskForm()
    return render(request, 'qa/ask_page.html',{'form':form,'user':request.user})

def answer(request):
        if request.method == 'POST':
            form = AnswerForm(request.POST)
            if form.is_valid():
                form._user=request.user
                answer=form.save()
                url='/question/'+str(answer.question.pk)
                return HttpResponseRedirect(url)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
        return HttpResponseRedirect('/')
    return render(request,'qa/login_page.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username,email,password)
        return HttpResponseRedirect('/')
    return render(request, 'qa/signup_page.html')
