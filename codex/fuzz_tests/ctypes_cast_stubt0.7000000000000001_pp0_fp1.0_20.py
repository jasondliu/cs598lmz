import ctypes
ctypes.cast(id(0), ctypes.py_object).value

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, platform
import re
import ctypes
import struct
import gc
import time, datetime
import traceback
import itertools
import functools
import multiprocessing
import concurrent.futures
import csv, json

from enum import Enum
from threading import Thread, Lock

from PyQt5.Qt import QUrl, QDir, QFile, QFileInfo, QSettings, QTranslator, QLibraryInfo
from PyQt5.Qt import QStandardPaths, QSize, Qt, QRect, QPoint, QMargins
from PyQt5.Qt import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton
from PyQt5.Qt import QProgressDialog, QMessageBox, QInputDialog, QFileDialog, QDialog, QShortcut
from PyQt5.
