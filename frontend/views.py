from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BusinessForm
from django.contrib import messages
from .models import Business
from django.core.mail import send_mail
from django.conf import settings
from .partner_school_form import PartnerSchoolForm
from .models import PartnerSchool  # Make sure to import your model
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

    if request.method == 'POST':
        form = PartnerSchoolForm(request.POST)
        if form.is_valid():
            # Creating a new PartnerSchool model instance with form's cleaned data
            new_school = PartnerSchool(
                destination_country=form.cleaned_data['destination_country'],
                school_name=form.cleaned_data['school_name'],
                contact_first_name=form.cleaned_data['contact_first_name'],
                contact_last_name=form.cleaned_data['contact_last_name'],
                contact_email=form.cleaned_data['contact_email'],
                phone_number=form.cleaned_data.get('phone_number', 'N/A'),  # Handling optional fields
                contact_title=form.cleaned_data['contact_title'],
                referral_check=form.cleaned_data.get('referral_check', False),
                additional_comments=form.cleaned_data.get('additional_comments', 'N/A'),
            )
            new_school.save()  # Saving the model instance to the database

            # Preparing email content
            subject = 'Partner School Form Submitted'
            message = f"""
            New Submission Details:
            Destination Country: {new_school.destination_country}
            School Name: {new_school.school_name}
            Contact Name: {new_school.contact_first_name} {new_school.contact_last_name}
            Contact Email: {new_school.contact_email}
            Phone Number: {new_school.phone_number}
            Contact Title: {new_school.contact_title}
            Referred by Someone in Admission Platform: {'Yes' if new_school.referral_check else 'No'}
            Additional Comments: {new_school.additional_comments}
            """
            # Send email
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['partners@admissionplatform.io'],  # Replace with your actual recipient email
                fail_silently=False,
            )

            messages.success(request, 'Form submitted successfully!')
            return redirect('form_success')  # Make sure 'form_success' is a valid URL name in your urls.py
    else:
        form = PartnerSchoolForm()

    return render(request, 'schools.html', {'page_name': page_name, 'form': form})


def form_success(request):
    return render(request, 'form_success.html')


def new_associate(request):
    page_name = "Recruitment Partners"

    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new Business object and save the form data
            new_business = Business(
                business_certificate=form.cleaned_data['business_certificate'],
                business_logo=form.cleaned_data.get('business_logo'),  # Using .get() as it's optional
                owner_first_name=form.cleaned_data['owner_first_name'],
                owner_last_name=form.cleaned_data['owner_last_name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                preferred_contact_method=form.cleaned_data['preferred_contact_method'],
                how_found=form.cleaned_data['how_found'],
                referred_by=form.cleaned_data.get('referred_by', ''),
                recruiting_year=form.cleaned_data['recruiting_year'],
                source_country=form.cleaned_data['source_country'],
                services_provided=form.cleaned_data['services_provided'],
            )
            new_business.save()

            # Prepare email content
            subject = 'Partner Registration Form Submitted'
            message = f"""
            
            Owner's Name: {form.cleaned_data['owner_first_name']} {form.cleaned_data['owner_last_name']}
            Email: {form.cleaned_data['email']}
            Phone Number: {form.cleaned_data['phone_number']}
            Preferred Contact Method: {form.cleaned_data['preferred_contact_method']}
            How did you find out about Admission Platform?: {form.cleaned_data['how_found']}
            Has anyone at Admission Platform referred you? If yes, who? (optional):: {form.cleaned_data['referred_by']}
            In which year did you begin recruiting students?: {form.cleaned_data['recruiting_year']}
            Source Country: {form.cleaned_data['source_country']}
            Services Provided: {form.cleaned_data['services_provided']}
            """
            
            # Send email
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['partners@admissionplatform.io'],  # Replace with the target email address
                fail_silently=False,
            )
        
            
            messages.success(request, 'Form submitted successfully!')
            return redirect('form_success')
    else:
        form = BusinessForm()

    return render(request, 'new_associate.html', {'page_name': new_associate, 'form': form})


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

def findhighjob(request):
    page_name = "Find High-Job-Demand Study Options with Program Tags"
    return render(request, 'findhighjob.html', {'page_name': page_name})

def oursolutions(request):
    page_name = "oursolutions"
    return render(request, 'oursolutions.html', {'page_name': page_name})

def studyinuk(request):
    page_name = "Study in UK"
    return render(request, 'studyinuk.html', {'page_name': page_name})

def whyadmissionplatform(request):
    page_name = "Why Admission Platform"
    return render(request, 'whyus.html', {'page_name': page_name})

def missionvision(request):
    page_name = "Mission and Vision"
    return render(request, 'mission-vision.html', {'page_name': page_name})

def ourvalue(request):
    page_name = "Our Value"
    return render(request, 'our-value.html', {'page_name': page_name})

def globalrecognition(request):
    page_name = "Global Recognition"
    return render(request, 'global-recognition.html', {'page_name': page_name})

def events(request):
    page_name = "Events"
    return render(request, 'events.html', {'page_name': page_name})

def australia(request):
    page_name = "Australia"
    return render(request, 'australia.html', {'page_name': page_name})

def whyaustralia(request):
    page_name = "Why Study in Australia"
    return render(request, 'why-australia.html', {'page_name': page_name})

def australiapartner(request):
    page_name = "Australia: Partner Universities & Colleges"
    return render(request, 'australia-partner.html', {'page_name': page_name})

def canada(request):
    page_name = "Canada"
    return render(request, 'canada.html', {'page_name': page_name})

def canadapartner(request):
    page_name = "Canada: Partner Universities & Colleges"
    return render(request, 'canada-partner.html', {'page_name': page_name})

def whycanada(request):
    page_name = "Why Study in Canada"
    return render(request, 'why-canada.html', {'page_name': page_name})

def newzealand(request):
    page_name = "New Zealand"
    return render(request, 'newzealand.html', {'page_name': page_name})

def nzpartner(request):
    page_name = "New Zealand: Partner Universities & Colleges"
    return render(request, 'newzealand-partner.html', {'page_name': page_name})

def whynewzealand(request):
    page_name = "Why Study in Newzealand"
    return render(request, 'why-newzealand.html', {'page_name': page_name})

def unitedkingdom(request):
    page_name = "United Kingdom"
    return render(request, 'unitedkingdom.html', {'page_name': page_name})

def whyuk(request):
    page_name = "Why Study in UK"
    return render(request, 'why-uk.html', {'page_name': page_name})

def ukpartner(request):
    page_name = "United Kingdom: Partner Universities & Colleges"
    return render(request, 'uk-partner.html', {'page_name': page_name})

def unitedstates(request):
    page_name = "United States"
    return render(request, 'unitedstates.html', {'page_name': page_name})

def whyusa(request):
    page_name = "Why Study in USA"
    return render(request, 'why-usa.html', {'page_name': page_name})

def usapartner(request):
    page_name = "United States: Partner Universities & Colleges"
    return render(request, 'usa-partner.html', {'page_name': page_name})

def team(request):
    page_name = "Meet the Team"
    return render(request, 'team.html', {'page_name': page_name})


def australiaresources(request):
    page_name = "Resources"
    return render(request, 'australia-resources.html', {'page_name': page_name})