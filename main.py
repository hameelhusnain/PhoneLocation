import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.prase(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)


from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

# Add the OpenCage API's Key here. (Never share this key with anyone)
key = '-------------------'

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
#print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start= 9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")