from django.shortcuts import render, redirect, reverse
from ..login.models import User


def current_user(request):
	return User.objects.get(id=request.session['user_id'])

def index(request):
	try:
		request.session['user_id']
	except KeyError:
		return redirect('/')
	context = {
		'user': User.objects.get(id=request.session['user_id'])
	}
	return render(request, 'wall/index.html', context)

# def personal(request, user):
# 	context = {
# 		'quote': Quote.objects.get(id=id)
# 	}
# 	return render(request, 'wall/personal.html')

def quotes(request):
	if request.method == "POST":
		#Validate form data
		errors = Water.objects.validate(request.POST)

		#if no errors
		if not errors:
			#Get the currently logged in user
			user = current_user(request)
			#Create the new post
			quote = Quote.objects.create_quote(request.POST, user)
			#Redirect back to same page 
			return redirect(reverse('dashboard'))

		#flash errors

	return redirect(reverse('dashboard')) 