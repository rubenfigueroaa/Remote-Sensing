import geopandas as gpd
import matplotlib.pyplot as plt
#Load the KML File
kml_file = "C:/Users/Ruben/OneDrive/Escritorio/RemoteSensing/Polygon Data/Huerta La Colmena.kml"
huerta = gpd.read_file(kml_file, driver = 'KML')

#Print the contents to inspect
print(huerta)

#Metric CRS for accurate Area Calculation
huerta_metric = huerta.to_crs(epsg = 32612) #EPSG code for Northern Sonora Region

#Area calculation
huerta['area_m2'] = huerta_metric['geometry'].area
huerta['area_ha'] = huerta['area_m2'] / 1000 #Convert square meters to hectareas

#Print the calculated area
print(f"Area in square meters : {huerta['area_m2'].iloc[0]:,.2f}")
print(f"Area in hectares: {huerta['area_ha'].iloc[0]:,.2f}")

#Save data to GeoJson File
huerta.to_file("huerta_with_area.geojson", driver = "GeoJSON")

#Polygon Visualization
huerta_metric.plot()
plt.title("Huerta La Colmena Boundary")
plt.show()