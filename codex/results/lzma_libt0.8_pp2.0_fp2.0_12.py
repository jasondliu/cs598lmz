import lzma
lzma.decompress

import sys
sys.path.append('C:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\arcgispro-py3\\Lib\\site-packages\\')
import rasterio
import rasterio.features
sys.path.append(os.path.join(sys.path[-1], 'Scripts'))
import fiona

import geopandas as gpd


try:
    from .get_poly_files import get_poly_files
except:
    from get_poly_files import get_poly_files

def get_extent(srs, geom):
    xmin,ymin,xmax,ymax = geom.bounds
    ring = ogr.Geometry(ogr.wkbLinearRing)
    ring.AddPoint(xmin, ymin)
    ring.AddPoint(xmax, ymin)
    ring.AddPoint(xmax, ymax)
    ring.AddPoint(xmin, ymax)
    ring.AddPoint(xmin, ymin)
   
