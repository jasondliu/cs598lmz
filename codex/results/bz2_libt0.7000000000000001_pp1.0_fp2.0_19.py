import bz2
bz2.decompress(data)

with open('geotowns.pickle', 'rb') as f:
    geo_towns = pickle.load(f)

with open('towns_coords.pickle', 'rb') as f:
    towns_coords = pickle.load(f)

with open('distances.pickle', 'rb') as f:
    distances = pickle.load(f)

with open('towns_to_process_coords.pickle', 'rb') as f:
    towns_to_process_coords = pickle.load(f)

with open('geotowns_to_process.pickle', 'rb') as f:
    geotowns_to_process = pickle.load(f)

with open('clusters.pickle', 'rb') as f:
    clusters = pickle.load(f)

with open('clusters_to_process.pickle', 'rb') as f:
    clusters_to_process = pickle.load(f)
    
with open('
