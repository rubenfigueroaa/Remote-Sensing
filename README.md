# Remote-Sensing
Introduction to Remote Sensing Manipulation and Data Analysis

v.0.0 FIRST INTERACTION WITH REMOTE SENSING: Area Calculation
Google Earth Pro is a high fidelity satellite imaging portal, and for my first exercise, we will use the polygon drawing function inside the software to represent the area of an Orange Orchard in Sonora, México.
![Captura de pantalla 2025-01-06 105528](https://github.com/user-attachments/assets/3221e387-32a0-42eb-8f71-e705e0b7873b)

After drawing the polygon, the data will be saved as a KML file for future handling.
Inside huertaColmena.py, the KML file is handled using the geopandas Library to read the file and process the accurate Area Calculation. 

Finally, the data is stored in a GeoJson File and plotted the boundaries using the matplotlib library.

RESULTS: 
![Boundary Visualization](https://github.com/user-attachments/assets/e2f691c6-ba3c-42d7-92a6-87d6af8a7ff1)
![Results Python Code](https://github.com/user-attachments/assets/d626a6e7-2a0a-43ac-96f4-38d1afed2cdc)
And the estimated from the code is verified directly with the Google Earth Pro Polygon Data already in the software,![Google Earth Verification](https://github.com/user-attachments/assets/eed0f0af-49bf-48c5-808e-ea285c4fa819)


