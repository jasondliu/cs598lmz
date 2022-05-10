import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import os
import sys
import glob
import time
import shutil
import datetime
import subprocess
import numpy as np

# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from pix4d_orthomosaic_dialog import Pix4DOrthomosaicDialog
import os.path
import time
import re
import shutil
import datetime
import subprocess
import numpy as np
import math
import osgeo.gdal as gdal
from osgeo.gdalconst import *
import osgeo.ogr as ogr
import osgeo.osr as osr
import gdalnumeric
import gdalconst
import scipy.misc
import scipy.ndimage

