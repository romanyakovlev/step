# coding: utf-8
from django import forms
from qa.models import Question,Answer

class AskForm(forms.Form):
	title=forms.CharField(max_length=100)
	text=forms.CharField(widget=forms.Textarea)

	def clean(self):
		if self._errors:
			raise forms.ValidationError('ValidationError', code='invalid')
	def save(self):
		self.cleaned_data['author']=self._user
		ask=Question(**self.cleaned_data)
		ask.save()
		return ask

class AnswerForm(forms.Form):
	text=forms.CharField(widget=forms.Textarea)
	question=forms.IntegerField(widget=forms.HiddenInput())

	def clean(self):
		if self._errors:
			raise forms.ValidationError(_('ValidationError'), code='invalid')

	def save(self):
		self.cleaned_data['question']=Question.objects.get(id=self.cleaned_data['question'])
		self.cleaned_data['author']=self._user
		answer=Answer(**self.cleaned_data)
		answer.save()
		return answer
