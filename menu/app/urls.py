from django.urls import path

from .views import base


urlpatterns = [
    path('home/', base, {'name': 'Home'}, name='home'),
    path('about/', base, {'name': 'About Us'}, name='about Us'),
    path('services/', base, {'name': 'Services'}, name='services'),
    path('web_development', base, {'name': 'Web Development'}, name='web development'),
    path('web_development/front', base, {'name': 'Front-end Development'}, name='front'),
    path('web_development/back', base, {'name': 'Back-end Development'}, name='back'),
    path('services/mobile', base, {'name': 'Mobile App Development	'}, name='mobile'),
    path('services/design', base, {'name': 'UI-UX Design'}, name='design'),
    path('portfolio/', base, {'name': 'Portfolio'}, name='portfolio'),
    path('blog/', base, {'name': 'Blog'}, name='blog'),
    path('contact/', base, {'name': 'Contact'}, name='contact'),
]
