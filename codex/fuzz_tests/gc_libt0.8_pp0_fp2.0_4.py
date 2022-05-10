import gc, weakref
import numpy as np
import time
import os, sys
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg

from PyQt5.QtCore import QObject, pyqtSignal, Qt
from PyQt5.QtSvg import QSvgGenerator

from CellExplorer.class_parameters import *
from CellExplorer.utils import *
from CellExplorer.cache import *
from CellExplorer.processing import *
from CellExplorer.gui.browser import *
from CellExplorer.gui.display_widget import *
from CellExplorer.gui.stats_widget import *

from CellExplorer.gui.plot_widget import *
from CellExplorer.gui.image_tab_widget import *
from CellExplorer.
