import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
from datetime import datetime
import pandas as pd
import numpy as py
from math import radians, cos, sin, asin, sqrt
from math import isnan
from geopy.geocoders import Nominatim as ns

path = "."

df_taxi_ijanta = pd.read_csv(os.path.join(path,"2019_Yellow_Taxi_Trip_Data.csv"))
print(df_taxi_ijanta.shape)
df_taxi_ijanta.head()



import re
from shapely.geometry import Point
import shapely.wkt

def dec2posit(decvalue):
    strvalue=str(decvalue)
    deg = float(strvalue[0:strvalue.find(".")])
    min = float(strvalue[strvalue.find(".")+1:])/ 60
    posit = deg + min
    return posit

import geopandas as gpd
