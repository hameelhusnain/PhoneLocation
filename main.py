import phonenumbers
import opencage
from myphone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.prase(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)


from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

key = '58aeced208bc43d8bad96d1cf285c9ea'

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder