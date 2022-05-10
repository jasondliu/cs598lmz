import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#QtCore.pyqtRemoveInputHook()
#import pdb ; pdb.set_trace()

from PySide import QtGui
from PySide import QtCore
from PySide.QtCore import Slot, Qt
from PySide.QtGui import QPainter, QBrush, QPen, QFont, QLinearGradient, QRadialGradient, QConicalGradient



from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.misc import imread
import cv2
from skimage.feature import hog
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from skimage import data, color, exposure
#from skimage.feature import hog
from
