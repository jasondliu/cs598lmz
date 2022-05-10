import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'), daemon=True).start()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import scipy
import math
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings("ignore")

import folium
from folium import plugins
from folium.plugins import HeatMap

# !pip install geopy
from geopy.geocoders import Nominatim

# !pip install geocoder
import geocoder

# !pip install geopandas
import geopandas as gpd

import requests

# !pip install shapely
import shapely.geometry
import shapely.ops

