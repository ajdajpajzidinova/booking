from django.urls import path, include
from rest_framework.routers import *
from .views import *


urlpatterns = [
    path('country/', CountryListAPIView.as_view()),
    path('country/<int:pk>/', CountryDetailAPIView.as_view()),

    path('city/', CityListAPIView.as_view()),
    path('city/<int:pk>/', CityDetailAPIView.as_view()),

    path('service/', ServiceListAPIView.as_view()),
    path('service/<int:pk>/', ServiceDetailAPIView.as_view()),

    path('hotel/', HotelListAPIView.as_view()),
    path('hotel/<int:pk>/', HotelDetailAPIView.as_view()),

    path('room/', RoomListAPIView.as_view()),
    path('room/<int:pk>/', RoomDetailAPIView.as_view()),

    path('review/', ReviewListAPIView.as_view()),

    path('booking/', BookingListAPIView.as_view()),

    path('user/', UserProfileListAPIView.as_view()),
    path('user/<int:pk>/', UserProfileDetailAPIView.as_view()),
    path('users/', UserProfileListAPIView.as_view(), name='users'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

