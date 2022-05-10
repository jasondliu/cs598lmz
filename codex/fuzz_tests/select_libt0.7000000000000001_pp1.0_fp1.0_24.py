import select
import sys
import time
import os
import datetime

from PyQt4.QtCore import QTimer
from PyQt4.QtGui import QApplication, QImage, QPainter, QWidget, QLabel, QPixmap
from resources.Camera import Camera
from threading import Thread, Event
from scipy import ndimage

from resources.Detector import Detector
from resources.PID import PID
from resources.TrackBar import TrackBar
from resources.Util import Util
from resources.WebServer import WebServer
import platform
import subprocess

import numpy as np
from skimage.morphology import reconstruction
from skimage.util import invert
from skimage.morphology import opening
from skimage.morphology import disk
from scipy.spatial.distance import pdist
from skimage.filters import threshold_otsu
from skimage.filters.rank import median
from skimage.morphology import remove_small_objects
from skimage.segmentation import clear_border
from skimage.measure import regionprops
from skimage.
