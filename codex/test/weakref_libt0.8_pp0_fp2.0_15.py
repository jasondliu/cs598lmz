import weakref
import pickle
import copy
import csv
import cv2
import os
import sys

import numpy as np

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from libs.utils import *
from libs.shape import *
from libs.settings import *
from libs.stringBundle import StringBundle
from libs.canvas import Canvas
from libs.zoomWidget import ZoomWidget
from libs.labelDialog import LabelDialog
from libs.colorDialog import ColorDialog
from libs.labelFile import LabelFile, LabelFileError
from libs.toolBar import ToolBar
from libs.pascal_voc_io import PascalVocReader
from libs.yolo_io import YoloReader
from libs.ustr import ustr
from libs.hashableQListWidgetItem import HashableQListWidgetItem


class WindowMixin(object):

    def menu(self, title, actions=None):
        menu = self
