import geopandas as gpd

gdf = gpd.read_file("flightmap_europe_fir_uir_ec_only.json")

# Filtrer uniquement les FIR françaises (codes commençant par "LF" et finissant par "FIR")
fr_fir = gdf[gdf["AV_AIRSPAC"].str.startswith("LF") & gdf["AV_AIRSPAC"].str.endswith("FIR")]

# Exporter
fr_fir.to_file("FIR_France_OFFICIEL.geojson", driver="GeoJSON")
print("✅ Export FIR France terminé")
