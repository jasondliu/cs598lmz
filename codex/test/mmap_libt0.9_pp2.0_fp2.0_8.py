import mmap
import json

nodes_by_id = {}
cities_by_osm_id = {}
min_lat = 179.0
min_lon = 179.0
max_lat = -179.0
max_lon = -179.0

with open("belarus-latest.osm.pbf") as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    reader = RawBlobReader(mm)
    i = 0
