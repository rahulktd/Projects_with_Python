from geopy.geocoders import Nominatim

geo_locator = Nominatim(user_agent="geoapiExercises")

place = input("Enter the city: ")

location = geo_locator.geocode(place)

print(location)