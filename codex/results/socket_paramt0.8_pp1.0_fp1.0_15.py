import socket
socket.if_indextoname(2)

```

```python
%matplotlib inline

import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from osgeo import gdal
import fiona
import rasterio
import rasterio.plot
from rasterio.plot import show
from rasterio.mask import mask

from os import system

from matplotlib import pyplot
import matplotlib.pyplot as plt

from shapely.geometry import Point, Polygon
from shapely.geometry.polygon import LinearRing, LineString
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA

import seaborn as sns

from scipy import stats
from scipy.stats import norm

from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import normalize
from sklearn.model_selection import train_test_split
from sklearn
