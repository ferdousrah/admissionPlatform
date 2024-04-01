from django.urls import path
from . import views


urlpatterns = [
    #path('home/', views.home, name='home'),
    path('', views.say_hello, name='say_hello'),
    path('studyabroad/', views.studyabroad, name='studyabroad'),
    path('recruiters/', views.recruiters, name='recruiters'),
    path('schools/', views.schools, name='schools'),
    path('new_associate/', views.new_associate, name='new_associate'),
    path('account/', views.account, name='account'),
    path('register/', views.register, name='register'),
    path('story/', views.story, name='story'),
    path('careers/', views.careers, name='careers'),
    path('blog/', views.blog, name='blog'),
    path('press/', views.press, name='press'),
    path('life/', views.life, name='life'),
    path('leadership/', views.leadership, name='leadership'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('fees/', views.fees, name='fees'),
    path('statement/', views.statement, name='statement'),
    path('ielts-writing/', views.ieltswriting, name='ielts-writing'),
    path('affordablecities/', views.affordablecities, name='affordablecities'),
    path('our-solutions/', views.oursolutions, name='oursolutions'),
    path('study-in-uk/', views.studyinuk, name='studyinuk'),
]