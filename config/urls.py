"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

# from django_test_api_001.views import ViewDetail_One, ViewDetail_Two, ViewDetail_Three
from django_test_api_001.views import ViewDetail_One, ViewDetail_Two, ViewDetail_Three

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),

    # path('api/statistics/employee/<int:pk>/?month=1&year=<int:year>/', ViewDetail_One.as_view()),
    # path('api/employee/statistics/?month=1&year=<int:year>/', ViewDetail_Two.as_view()),
    # path('api/statistics/client/<int:pk>/?month=1&year=<int:year>/', ViewDetail_Three.as_view()),


    # path('api/statistics/employee/<int:pk>/?month=<int:month>&year=<int:year>', ViewDetail_One.as_view()),
    # path('api/statistics/employee/<int:pk>/?month=<int:month>&year=<int:year>', ViewDetail_One.as_view()),
    # path('api/statistics/employee/<int:pk>', viewDetail_One),
    # path('api/statistics/employee/<int:pk>/?month=<int:month>&year=<int:year>', ViewDetail_One.as_view()),
    # path('api/statistics/employee/<int:pk>/month=<int:month>&year=<int:year>', ViewDetail_One.as_view()),
    path('api/statistics/employee/<int:pk>/month=<int:month>&year=<int:year>', ViewDetail_One.as_view()),
    path('api/employee/statistics/month=<int:month>&year=<int:year>', ViewDetail_Two.as_view()),
    path('api/statistics/client/<int:pk>month=<int:month>&year=<int:year>', ViewDetail_Three.as_view()),


    # path('api/statistics/employee/<int:pk>/?month=<int:month>&year=<int:year>', ViewDetail_One.as_view()),
    # path('api/employee/statistics/?month=<int:month>&year=<int:year>', ViewDetail_Two.as_view()),
    # path('api/statistics/client/<int:pk>?month=<int:month>&year=<int:year>', ViewDetail_Three.as_view()),


    # path('api/statistics/employee/<int:pk>', ViewDetail_One.as_view()),
    # path('api/employee/statistics', ViewDetail_Two.as_view()),
    # path('api/statistics/client/<int:pk>', ViewDetail_Three.as_view()),
    # path('api/statistics/client/<yyyy:year>', ViewDetail_Two.as_view()),
    # path('api/statistics/client/<YYYY-MM-DD:year>', ViewDetail_Two.as_view()),
    # path('users/', ListCreateAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='user-list'),


]

urlpatterns = format_suffix_patterns(urlpatterns)
