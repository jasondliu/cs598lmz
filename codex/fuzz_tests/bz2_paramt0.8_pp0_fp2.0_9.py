from bz2 import BZ2Decompressor
BZ2Decompressor.decompress
import geopy
from itertools import repeat
import dask.bag as db
from dask.diagnostics import ProgressBar, Profiler, ResourceProfiler, CacheProfiler
from dask.diagnostics.profile_visualize import visualize
%matplotlib inline
 
def get_buffered_points(record):
    """Fix a point geometry so that it is not just a single coordinate"""
    geom = GEOSGeometry(record['geometry'])
    return Point(geom.centroid.coords[0], geom.buffer(0.01))
osm_map = geopandas.read_file('/Users/ksatola/Downloads/planet-latest.osm.pbf')
osm_map = osm_map[osm_map.geometry.type == 'Point']
osm_map = osm_map.to_crs(epsg=4326)
 
osm_map['geometry'] = osm_map.apply(lambda x: get_buffered_points(x), axis=1)
osm_map.
