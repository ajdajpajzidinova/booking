from django.contrib import admin

from .models import (
    Country,
    UserProfile,
    City,
    Service,
    Hotel,
    HotelImage,
    Room,
    RoomImage,
    Review,
    Booking
)

admin.site.register(UserProfile)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Service)
admin.site.register(Review)
admin.site.register(Booking)


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('hotel_name', 'country', 'city', 'hotel_stars')
    inlines = [HotelImageInline]


class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'hotel', 'room_type', 'room_status', 'price')
    inlines = [RoomImageInline]