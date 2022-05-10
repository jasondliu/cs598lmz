import weakref

import cv2
import numpy as np
import pyqtgraph as pg

from pyqtgraph.Qt import QtGui, QtCore
from pyqtgraph.widgets.MatplotlibWidget import MatplotlibWidget

from matplotlib import pyplot as plt
from matplotlib import cm

import scipy.optimize as opt

from sklearn.metrics import mean_squared_error

from PYME.LMVis import genColourTable

from PYME.LMVis.shader_programs import *
from PYME.LMVis.layers import ImageLayer, Labels, LabelsLayer, VisPyCanvasLayer, VisPyCanvas
from PYME.LMVis.layouts import *
from PYME.LMVis.shader_programs.image_filter_shaders import gaussian_filter
# from PYME.LMVis.imageWidgets import ImageWidget, ImageWidget3D

from PYME.recipes.traits import CStr, Int, Float, Enum, List, Bool, Dict
