import mmap
import os
import sys
import time
import traceback

from collections import OrderedDict
from datetime import datetime
from functools import partial
from itertools import chain
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing.pool import ThreadPool as ProcessPool
from os.path import join, abspath, dirname, exists, isdir, isfile, splitext
from shutil import rmtree
from subprocess import Popen, PIPE
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets

from . import __version__
from .config import Config
from .constants import (
    APP_NAME,
    APP_VERSION,
    APP_URL,
    APP_AUTHOR,
    APP_AUTHOR_EMAIL,
    APP_DESCRIPTION,
    APP_LICENSE,
    APP_YEAR,
    APP_ICON,
    APP_ICON_PATH,
    APP_LOGO,
    APP_
