from typing import ContextManager
from django import template

from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserForm

def Home(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Thanks(request):
    context = {}
    return render(request, 'thanks.html', context)

def Signup(request):
    if request.method == 'POST':
        # above code is using the forms.form create
        # form = NameForm(request.POST)
        # using the form from modelform created
        form = UserForm(request.POST)
        # process the form data
        if form.is_valid():
            # validate the form data
            # redirect to a new url:
            form.save()
            # Using the full http redirect
            # return HttpResponseRedirect('thanks')
            # using the shortcut redirect
            return redirect('thanks')
    else:
        # render a blank form
        form = UserForm()

    # template = loader.get_template('signup.html')
    context = {
        'form': form
    }

    # return HttpResponse(template.render(template, context))
    return render(request, 'signup.html', context)