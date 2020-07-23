import folium



map = folium.Map(location = [40.7864, 17.2409], zoom_start=6, tiles = "OpenStreetMap")

fgv = folium.FeatureGroup(name="To Visit")

fgv.add_child(folium.Marker(location = [40.7864, 17.2409], popup = "Arbelobello,Italy", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [43.7696, 11.2558], popup = "Florence,Italy", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [43.8429, 10.5027], popup = "Lucca,Italy", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [40.3980, 17.6377], popup = "Manduria,Italy", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [40.3515, 18.1750], popup = "Lecce,Italy", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [44.1116, 9.7339], popup = "Manarola,Italy", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [42.6826, 11.7142], popup = "Sorano,Italy", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [-20.2067, 57.5522], popup = "Mauritius", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [50.0647, 19.9450], popup = "Krakow, Poland", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [44.4056, 8.9463], popup = "Genoa,Italy", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [41.9794, 2.8214], popup = "Girona,Spain", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [41.3851, 2.1734], popup = "Barcelona,Spain", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [-2.3326, 34.6857], popup = "Serengeti,Tanzania", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [52.3667, 4.8945], popup = "Amsterdam,Netherlands", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [57.4737, -4.0918], popup = "Culloden,Scotland", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [42.6507, 18.0944], popup = "Dubrovnik,Crotaia", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [48.8566, 2.3522], popup = "Paris,France", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [28.6050, -80.6026], popup = "Kennedy Space Center,USA", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [-38.2619, 175.0986], popup = "Waitomo,New Zealand", icon = folium.Icon(color="cadetblue", icon="briefcase")))
fgv.add_child(folium.Marker(location = [41.9047, 12.4547], popup = "Vatican City,Italy", icon = folium.Icon(color="cadetblue", icon="briefcase")))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map.html")