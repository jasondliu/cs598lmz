import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib.ticker as ticker
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
from matplotlib.ticker import FuncFormatter
from matplotlib.widgets import Slider, Button
from matplotlib.widgets import CheckButtons
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import TextBox

import numpy as np
import pandas as pd

import sys
import os
import time
import random
import datetime
import json

import warnings
warnings.filterwarnings('ignore')

import ipywidgets as widgets
from ipywidgets import Layout, HBox, VBox, Box, Button, Text, Label, RadioButtons, Checkbox, Dropdown, HTML, IntSlider, FloatSlider, BoundedIntText, BoundedFloatText, Accordion, ToggleButton, Textarea
