# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView 
from .forms import FirstForm


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'
class FirstFormView(TemplateView):
    template_name = 'fform.html'
class SubmitedView(TemplateView):
    template_name = 'submitted.html'

def first_form(request):
    if request.method == 'POST':
    	# create a form instance and populate it with data from the request:
    	form = FirstForm(request.POST, request.FILES)
    	# check whether it's valid:
    	if form.is_valid():
    		data = form.cleaned_data
    		csv_file = request.FILES["csv"]
    		# if not csv_file.name.endswith('.csv'):
    		# 	messages.error(request,'File is not CSV type')
    		# 	return render(request, 'fform.html', {'form': form})
	        #if file is too large, return
	        # if csv_file.multiple_chunks():
	        # 	messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
	        # 	return render(request, 'fform.html', {'form': form})
	        # form.save()
	        file_data = csv_file.read().decode("utf-8")
	        return render(request, 'submitted.html', {'request': form, 'csv':csv_file,'file_data':file_data})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = FirstForm()

    return render(request, 'fform.html', {'form': form})

# Create your views here.
def submited(request): 
    return HttpResponse('Hello, World!')
# Create your views here.
def homePageView(request): 
    return HttpResponse('Hello, World!')