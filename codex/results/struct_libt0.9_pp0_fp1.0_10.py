import _struct

import ctypes
from ctypes import wintypes

import sys
from multiprocessing import Process, Queue, Value, Array
from queue import Empty, Full
from time import time, sleep
import datetime as dt
import os
from os.path import realpath, dirname, join
from subprocess import Popen, call

from threading import Thread, Event
import re
from shapely.geometry import Polygon, MultiPolygon, box, Point, LineString
from shapely.validation import explain_validity

from PyQt5.QtCore import QThread, pyqtSignal

from qgis.core import QgsMessageLog, Qgis, QgsProject, QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsPointXY, QgsWkbTypes, QgsCoordinateReferenceSystem, QgsFeatureSink, QgsProcessingFeedback, QgsProcessingException, QgsMessageLog, QgsProcessingUtils
from qgis.core import QgsCoordinateTransform, QgsProcessing, QgsProcessingAlgorithm
