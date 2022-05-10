import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtWebKit import QWebView
from PyQt4.QtNetwork import QNetworkRequest
from PyQt4.QtCore import QUrl
from PyQt4.QtCore import QByteArray
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QImage
from PyQt4.QtGui import QPainter
import time
from PyQt4.QtCore import QTimer
from pyvirtualdisplay import Display

from urllib import urlopen
from urlparse import urlparse
from urlparse import urlunparse
from os.path import basename
import re
from PIL import Image
import cStringIO
from io import BytesIO
import cv2
import numpy as np
import os
import json
from datetime import datetime
import math
from operator import itemgetter

from selenium import webdriver

