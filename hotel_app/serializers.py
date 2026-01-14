from rest_framework import serializers
from .models import *

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name',
                  )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user



class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country_name', 'country_image']


class CountryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'



class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city_name', 'city_image']


class CityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'



class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service_name', 'service_image']


class ServiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'



class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'hotel_stars']


class HotelDetailSerializer(serializers.ModelSerializer):
    rooms = serializers.StringRelatedField(many=True, read_only=True)
    images = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = '__all__'



class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_number', 'price', 'room_type', 'room_status']


class RoomDetailSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Room
        fields = '__all__'



class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'hotel', 'rating', 'descriptions', 'created_date']



class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'



class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'user_role']


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
