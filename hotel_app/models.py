from phonenumber_field.modelfields import PhoneNumberField

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class Country(models.Model):
    country_image = models.ImageField(upload_to= 'country_img')
    country_name = models.CharField(max_length=40,unique=True)

    def __str__(self):
        return self.country_name


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(90)],
                                           null=True,blank=True)
    user_image = models.ImageField(upload_to='user_photo',null=True,blank=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
    phone_number = PhoneNumberField (null=True,blank=True)
    RoleChoices = (
    ('client','client'),
    ('owner','owner')
    )
    user_role = models.CharField(max_length=30,choices=RoleChoices,default='client')
    registered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name},{self.last_name}'

class City(models.Model):
    city_image = models.ImageField(upload_to='city_images')
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name


class Service(models.Model):
    service_image = models.ImageField(upload_to='service_images')
    service_name = models.CharField(max_length=50)

    def __str__(self):
        return self.service_name


class Hotel (models.Model):
    hotel_name = models.CharField(max_length=60)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    postal_code = models.PositiveSmallIntegerField(verbose_name='почтовый индекс')
    hotel_stars = models.PositiveSmallIntegerField(choices=[(i ,str(i))for i in  range (1,6)])
    descriptions = models.TextField()
    hotel_service = models.ManyToManyField(Service)

    def __str__(self):
        return self.hotel_name

class HotelImage (models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    hotel_images = models.ImageField(upload_to='hotel_images/')

    def __str__(self):
        return f'{self.hotel},{self.hotel_images}'

class Room (models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number= models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField()
    RoomTypeChoices = (
    ('Люкс','Люкс'),
    ('Полулюкс', 'Полулюкс'),
    ('Семейный', 'Семейный'),
    ('Эконом', 'Эконом'),
    ('Одноместный', 'Одноместный')
    )
    room_type = models.CharField(max_length=20,choices=RoomTypeChoices)
    RoomStatusChoices =  (
    ('Занят','Занят'),
    ('Забронирован','Забронирован'),
    ('Свободен','Свободен')
    )
    room_status = models.CharField(max_length=40,choices=RoomStatusChoices)

class RoomImage (models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_images = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return f'{self.room},{self.room_images}'

class Review (models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i ,str(i))for i in  range (1,11)])
    descriptions = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user},{self.hotel}'



class Booking (models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    chek_in = models.DateField()
    chek_out = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user},{self.hotel},{self.room}'
