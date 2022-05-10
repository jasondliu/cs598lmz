import ctypes
ctypes.cast(0, ctypes.py_object).value

# %%
import os
os.system('ls')

# %%
import sys
sys.platform

# %%
import time
time.ctime()

# %%
import random
random.random()

# %%
import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()

# %%
from xml.etree.ElementTree import parse
doc = parse(u)

# %%
for bus in doc.findall('bus'):
    d = bus.findtext('d')
    lat = float(bus.findtext('lat'))
    if lat > 41.980262:
        print(d, lat)

# %%
import json
serialized = """{ "title" : "Data Science Book",
                  "author" : "Joel Grus",
                  "publicationYear" : 2014,
                  "topics" : [ "data",
