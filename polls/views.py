from django.http import HttpResponse,HttpResponseRedirect 
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import F

from django.utils import timezone

from .models import Choice, Question


#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'polls/index.html', context)



#def index(request):
	#latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('polls/index.html')
	#context = {
	#	'latest_question_list' : latest_question_list, 	
	#}

	# used when no template was defined and give an unformatted output
	#output = ', '.join([ques.question_text for ques in latest_question_list])

	#return HttpResponse(template.render(context,request))

 	# Before creating the front end we write it as this:
	#return HttpResponse(output)

	# Leave the rest of the views (detail, results, vote) unchanged	
	#return HttpResponse("Hello, world. You're at the polls index.")



#def detail(request, question_id):
#	question = get_object_or_404(Question, pk=question_id)
#	return render(request, 'polls/detail.html', {'question': question})


# Used before	
	#try: 	
	#	question = Question.object.get(pk=question_id)
	#except Question.DoesNotExist: 
	#	raise Http404("Question doesn't exist")
	#return render(request, 'polls/detail.html', {'question':question})
	# This used to be the style when no front end was designed without exception handling	
	#return HttpResponse("You're looking at question %s." %question_id)We also created a dummy implementation of the vote() function. Let’s create a real version. Add the following to polls/views.py:




	
#def results(request, question_id):
#	question = get_object_or_404(Question,pk = question_id)
#	return render(request, 'polls/results.html', {'question': question})



#Dummy view of Results		
	#response = "You're looking at the results of question %s."
	#return HttpResponse(response % question_id)

#def vote(request, question_id):

#	question = get_object_or_404(Question, pk=question_id)


#	try:
#		selected_choice = question.choice_set.get(pk=request.POST['choice'])


#	except (KeyError, Choice.DoesNotExist):
		#Redisplay the question voting form.
#		return render(request,'polls/detail.html', {
#			'question':question, 				'error':"You didn't select a choice. ",				
#			})
	

#	else: 
#		selected_choice.votes = F('votes')+1
#		selected_choice.save()
		#Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button
#		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

		
#Dummy Implementation	
	#return HttpResponse("You're voting on question %s." %question_id)








#After adding generic views



class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	
	def get_queryset(self): 
		"""
    		Return the last five published questions (not including those set to be published in the future).
    		"""
		return Question.objects.filter(		
			pub_date__lte=timezone.now()
			).order_by('-pub_date')[:5]

class DetailView(generic.DetailView): 
	model = Question
	template_name = 'polls/detail.html'
	def get_queryset(self):
        	"""Excludes any questions that aren't published yet."""
        	return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'


def vote(request, question_id):

	question = get_object_or_404(Question, pk=question_id)


	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])


	except (KeyError, Choice.DoesNotExist):
		#Redisplay the question voting form.
		return render(request,'polls/detail.html', {
			'question':question, 				'error':"You didn't select a choice. ",				
			})
	

	else: 
		selected_choice.votes = F('votes')+1
		selected_choice.save()
		#Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

