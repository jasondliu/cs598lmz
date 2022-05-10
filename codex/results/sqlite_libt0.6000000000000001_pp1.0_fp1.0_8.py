import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import subprocess
import time
import datetime
import signal

try:
    import ujson as json
except ImportError:
    import json

try:
    import nltk
except ImportError:
    nltk = None

try:
    import numpy
except ImportError:
    numpy = None

try:
    import scipy
except ImportError:
    scipy = None

try:
    import scipy.stats
except ImportError:
    scipy.stats = None

try:
    import scipy.spatial
except ImportError:
    scipy.spatial = None

try:
    import scipy.cluster
except ImportError:
    scipy.cluster = None

try:
    import sklearn
except ImportError:
    sklearn = None

try:
    import sklearn.cluster
except ImportError:
    sklearn.cluster = None

try:
    import sklearn.decomposition
except ImportError:
    sklearn.
