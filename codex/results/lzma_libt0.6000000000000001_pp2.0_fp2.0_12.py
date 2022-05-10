import lzma
lzma.open

import os
os.path.exists

import psutil
psutil.Process

import pytest
pytest.raises

import requests
requests.get

import sqlite3
sqlite3.connect

import typing
typing.NamedTuple

import unittest
unittest.TestCase

import urllib
urllib.request.urlopen

from xml.etree import ElementTree
ElementTree.ElementTree

# Make sure the following are not imported, as it would require
# the user to install additional packages.

# import gi
# gi.require_version

# import lxml
# lxml.etree

# import numpy
# numpy.ndarray

# import pyside2
# pyside2.QtCore

# import PyQt5
# PyQt5.QtCore

# import PySide2
# PySide2.QtCore

# import scipy
# scipy.stats

# import sklearn
# sklearn.metrics
