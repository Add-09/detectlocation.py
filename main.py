import phonenumbers
from test import number
from phonenumbers import geocoder
ch_numbers = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_numbers, "en"))

from phonenumbers import carrier
service_numbers = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_numbers, "en"))