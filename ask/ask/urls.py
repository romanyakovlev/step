"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from qa.views import test, new_questions, pop_questions\
, question_detail, form_ask, answer, login_page, signup

urlpatterns = [
    url(r'^$',new_questions,name='new_questions'),
    url(r'^popular/',pop_questions,name='pop_questions'),
    url(r'^question/(?P<pk>\w+)/',question_detail,name='question_detail'),
    url(r'^ask/',form_ask,name='form_ask'),
    url(r'^answer/',answer,name='answer'),
    url(r'^login/',login_page,name='login_page'),
    url(r'^signup/',signup,name='signup'),
    url(r'^new/',test,name='new'),
    url(r'^admin/', admin.site.urls),
]
