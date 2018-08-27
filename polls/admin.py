from django.contrib import admin


# Register your models here.
from .models import Choice, Question

#Replacing this admin.site.register(Question) with
# Replacing this ---> admin.site.register(Choice) with

class ChoiceInline(admin.TabularInline):
    	model = Choice
    	extra = 3

class QuestionAdmin(admin.ModelAdmin):
#Replacing this -----> fields = ['pub_date', 'question_text'] with 

	fieldsets = [
        	(None,               {'fields': ['question_text']}),
        	('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    	]
	inlines = [ChoiceInline]
	list_filter = ['pub_date']	
	list_display = ('question_text','pub_date','was_published_recently')
	search_fields = ['question_text']
 
admin.site.register(Question, QuestionAdmin)

