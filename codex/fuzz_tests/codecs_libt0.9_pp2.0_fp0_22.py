import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import csv
from zipfile import ZipFile
import pandas as pd
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
import Incentre_Data_Functions as IDF
from shapely.geometry import Point, shape
from pyproj import Proj, transform
from scipy.interpolate import griddata
from collections import OrderedDict

def update_colorbar(axes):
    axes[0].set_aspect('auto')
    x0,x1 = axes[0].get_xlim()
    y0,y1 = axes[0].get_ylim()
    axes[0].set_aspect(abs(x1-x0)/abs(y1-y0))
    
def get_coordinates(features, name):
    key = features[0][name]
    coordinates = features[1].split(",")
    return key, coordinates

#A function
