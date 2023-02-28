import geopandas as gpd
import matplotlib.pyplot as plt

# Cargar la capa temática
natalidad = "datos/natalidad.geojson"
map_data = gpd.read_file(natalidad)
map_data.head()