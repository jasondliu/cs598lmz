import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# import classes and functions
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import Qt, QPoint
import numpy as np
import copy
from functools import partial
from PIL import Image, ImageChops
from PIL.ImageQt import ImageQt
import pyqtgraph as pg
from image_viewer import ImageViewer, ImageExplorer
from canvas import Canvas, TextNote
from objects import Object, SEGMENTATION, TRACE, SCREENSHOT, BOOKMARK, NOTE, OBJECT_KIND
from masking import MaskingArea
from mouse_actions import mouse_move_event, mouse_press_event, mouse_release_event
from keyboard_actions import keyboard_press_event, keyboard_release_event
from tools import MoveTool, PaintTool, ZoomTool
from images import sbig_icon_16, s
