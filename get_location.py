import geocoder
import folium

## you can replace the ip number with "me" for your actual location.
our_ip= geocoder.ip("161.185.160.93")
the_event= our_ip.latlng

our_map= folium.Map(location=the_event, zoom_start=10)
folium.Marker(the_event).add_to(our_map)

our_map.save("map.html")

print(our_ip, the_event)
