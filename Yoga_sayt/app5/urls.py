from django.urls import path, include
from .views import home,about_us , blog , contact , classes , elements
urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about_us, name='about-us'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('classes/', classes, name='classes'),
    path('elements/', elements, name='elements'),
    ]