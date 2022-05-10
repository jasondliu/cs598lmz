import ctypes
import ctypes.util
import threading
import sqlite3
import datetime

from face_detect import FaceDetect

from PIL import Image
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_face_detection import Ui_FaceDetection
from ui_face_recognition import Ui_FaceRecognition
from ui_face_database_new import Ui_FaceDatabaseNew
from ui_face_database_search import Ui_FaceDatabaseSearch
from ui_face_database_search_result import Ui_FaceDatabaseResult
from ui_face_settings import Ui_FaceSettings
from ui_face_threshold import Ui_FaceThreshold

from ui_face_database_chinese import Ui_FaceDatabaseChinese
from ui_face_recognition_chinese import Ui_FaceRecognitionChinese
