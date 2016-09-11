from django.shortcuts import render

from .forms import SignUpForm
from .models import SignUp

def home(request):
	title = 'Welcome'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form		
	}
	print request
	print request.POST
	
	if form.is_valid():
		#form.save()
		#print request.POST['email'] #not recommended, raw data without validation
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		# if not instance.full_name:
		# 	instance.full_name = "Justin"
		instance.save()
		context = {
			"title": "Thank you"
		}

	return render(request, "home.html", context)

def contact(request):
	form = ContactForm(request.POST or None)

	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		# 	#print form.cleaned_data.get(key)

	context = {
		"form": form,
	}
	return render(request, "forms.html", context)
