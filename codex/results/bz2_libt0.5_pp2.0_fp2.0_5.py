import bz2
bz2.decompress(bz2.BZ2File('../data/wikidata/wikidata-mappings-en.ttl.bz2').read())
 
# Using `rdflib`
from rdflib import Graph
g = Graph()
g.parse('../data/wikidata/wikidata-mappings-en.ttl', format='turtle')
len(g)
 
# Using `pandas`
from pandas import read_csv
read_csv('../data/wikidata/wikidata-mappings-en.csv.bz2')
 
# Using `sqlite3`
import sqlite3
conn = sqlite3.connect('../data/wikidata/wikidata-mappings-en.db')
 
# Using `json`
import json
with open('../data/wikidata/wikidata-mappings-en.json') as f:
    json.load(f)
 
# Using `h5py`
import h5py
h5py.File('../data/wikidata
