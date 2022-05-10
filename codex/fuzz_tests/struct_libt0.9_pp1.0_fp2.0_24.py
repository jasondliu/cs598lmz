import _struct as struct

import datetime as dt
import errno as os_errors
import glob as glob
import multiprocessing as mp
import numpy as np
import os as os
import rasterio as rio
import subprocess as subprocess
import sys as sys
import time as time
import traceback as traceb
# import threading as threading
import gdal as gdal
gdal.UseExceptions()
gdal.AllRegister()

import pyproj as pyproj

#sys.setrecursionlimit(40000)
# gdal.SetConfigOption("gdal_FILENAME_IS_UTF8", "YES")
gdal.SetConfigOption("SHAPE_ENCODING", "")

# import bokeh as bkh
# from bokeh.layouts import row, column
# from bokeh.models import CustomJS, Slider, ColumnDataSource, Span
# from bokeh.plotting import figure, output_file, show, save
# from bokeh.io import output_notebook

# # output_notebook()

#
