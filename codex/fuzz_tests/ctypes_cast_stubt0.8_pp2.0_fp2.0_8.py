import ctypes
ctypes.cast(0, ctypes.py_object).value = "Hello world!"

from IPython.core.display import HTML
from IPython.core.display import display

from string import Template
import pandas as pd
import json
from IPython.core.display import HTML
HTML("<iframe id='igraph' scrolling='no' style='border:none' seamless='seamless' src='http://localhost:8889/files/graph.html' height='600' width='100%'></iframe>")
 
# Set up the data for plotting. We will need to have values for every
# pair of year/month names. Map the rate to a color.
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
from matplotlib import cm as cm

import re
import json

data = []
f = open("data/explain.txt", "r")
for line in f:
    r = json.loads(line)
    data.append(r)
f.close
