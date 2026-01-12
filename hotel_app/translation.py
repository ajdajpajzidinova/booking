from modeltranslation.translator import register, TranslationOptions
from .models import Country, City, Service, Hotel, HotelImage, Room, RoomImage


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('service_name',)

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'street', 'descriptions')

@register(HotelImage)
class HotelImageTranslationOptions(TranslationOptions):
    fields = ()

@register(RoomImage)
class RoomImageTranslationOptions(TranslationOptions):
    fields = ()