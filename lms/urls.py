"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import index, blogs, contact, courses, about, team, course_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', include('lms_admin.urls')),
    path('', index, name='index'),
    path('blogs/', blogs, name='blogs'),
    path('courses/', courses, name='courses'),
    path('course/<int:id>', course_detail, name='course_detail'),
    path('about/', about, name='about'),
    path('team/', team, name='team'),
    path('contact/', contact, name='contact'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
