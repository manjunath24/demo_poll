from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings

from poll_app.models import PollQuestion, PollChoice, VoteTracker
from poll_app.forms import UserRegistrationForm, LoginForm, Profile


def index(request):
	polls = PollQuestion.objects.all()
	return render(request, 'home.html', {'polls': polls, 'home': True})


def detail(request, poll_id):
	poll = PollQuestion.objects.get(pk=poll_id)
	return render(request, 'detail.html', {'poll': poll})


@login_required
def vote(request, poll_id):
    poll = PollQuestion.objects.get(id=poll_id)
    choice_id = request.POST.get('choices')
    if not VoteTracker.objects.filter(poll=poll, user=request.user).exists():
	    choice = poll.pollchoice_set.get(id=choice_id)
	    choice.no_of_votes +=1
	    choice.save()
	    vote = VoteTracker.objects.create(poll=poll, user=request.user)
	    messages.success(request, 'You have successfully voted')
    else:
        messages.error(request, 'You have already voted')
    return redirect(reverse('detail', args=(poll.id,))) 


def registration(request):
	if request.method == "POST":
	    form = UserRegistrationForm(request.POST)
	    if form.is_valid():
	    	user = form.save()
            msg = EmailMessage('Hi', 'This is from localhost', settings.EMAIL_HOST_USER, [user.email])
            msg.send()
            messages.success(request, 'You are successfully registered')
            return redirect('registration')
	else:
		form = UserRegistrationForm()
	return render(request, 'registration.html', {'form': form, 'reg': True})


def signin(request):
    if request.method == "POST":
	    form = LoginForm(request.POST)
	    if form.is_valid():
	        username = form.cleaned_data['username']
	        password = form.cleaned_data['password']
	        user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Your account is not active')
                    return redirect('signin')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('signin')
    else:
        form = LoginForm()
        return render(request, 'sigin.html', {'form': form, 'signin': True})


@login_required
def delete(request, poll_id):
	poll = PollQuestion.objects.filter(id=poll_id).delete()
	return redirect('home')


def signout(request):
	request.session.flush()
	return redirect('home')


@login_required
def profile(request):
    if request.method == "POST":
        form = Profile(request.POST)
        if form.is_valid():
            user = request.user
            if 'first_name' in form.cleaned_data:
            	user.first_name = form.cleaned_data['first_name']
            if 'last_name' in  form.cleaned_data:
            	user.last_name = form.cleaned_data['last_name']
            if 'password' in form.cleaned_data:
            	user.set_password(form.cleaned_data['password'])
            user.save()

    else:
        form = Profile(initial={'first_name': request.user.first_name, 'last_name': request.user.last_name})
    return render(request, 'profile.html', {'form': form, 'profile': True})
