from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#def home(request):
#    return render(request, 'home.html')

def say_hello(request):
    return render(request, 'home.html')


def studyabroad(request):
    page_name = "Studyabroad"
    return render(request, 'studyabroad.html', {'page_name': page_name})


def recruiters(request):
    page_name = "Recruitment Partners"
    return render(request, 'recruiters.html', {'page_name': page_name})


def schools(request):
    page_name = "Institutions"
    return render(request, 'schools.html', {'page_name': page_name})


def new_associate(request):
    page_name = "Recruitment Partners"
    return render(request, 'new_associate.html', {'page_name': new_associate})


def account(request):
    page_name = "Sign In"
    return render(request, 'account.html', {'page_name': page_name})


def register(request):
    page_name = "Registration"
    return render(request, 'register.html', {'page_name': page_name})

def story(request):
    page_name = "Story"
    return render(request, 'story.html', {'page_name': page_name})

def careers(request):
    page_name = "Careers"
    return render(request, 'careers.html', {'page_name': page_name})

def blog(request):
    page_name = "Blog"
    return render(request, 'blog.html', {'page_name': page_name})

def press(request):
    page_name = "press"
    return render(request, 'press.html', {'page_name': page_name})

def life(request):
    page_name = "life"
    return render(request, 'life.html', {'page_name': page_name})

def leadership(request):
    page_name = "leadership"
    return render(request, 'leadership.html', {'page_name': page_name})

def contact(request):
    page_name = "contact"
    return render(request, 'contact.html', {'page_name': page_name})

def privacy(request):
    page_name = "privacy"
    return render(request, 'privacy.html', {'page_name': page_name})

def terms(request):
    page_name = "terms"
    return render(request, 'terms.html', {'page_name': page_name})

def fees(request):
    page_name = "fees"
    return render(request, 'fees.html', {'page_name': page_name})

def statement(request):
    page_name = "statement"
    return render(request, 'statement.html', {'page_name': page_name})


def ieltswriting(request):
    page_name = "ieltswriting"
    return render(request, 'ieltswriting.html', {'page_name': page_name})

def affordablecities(request):
    page_name = "affordablecities"
    return render(request, 'affordablecities.html', {'page_name': page_name})

def oursolutions(request):
    page_name = "oursolutions"
    return render(request, 'oursolutions.html', {'page_name': page_name})