import gmplot



lat = [26.472689,26.470192,26.466445,26.459046]
long = [73.114340,73.113834,73.115329,73.110477]

gmapone = gmplot.GoogleMapPlotter(26.472689,73.11430,15)

gmapone.scatter(lat,long,'red',size=50,marker=False)
gmapone.plot(lat,long,'blue',edge_width=2)
gmapone.draw('map.html')

