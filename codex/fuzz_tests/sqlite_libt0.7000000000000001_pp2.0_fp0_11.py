import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime
import os.path
import os
import platform
import sys
import shutil
import json
import zipfile
import inspect
import fnmatch
import locale

from debug import *
import debug


# The following are dummy functions for pyinstaller to include the required libraries

def dummy_pygtk():
	import pygtk
	return pygtk
	
def dummy_pango():
	import pango
	return pango
	
def dummy_gobject():
	import gobject
	return gobject

def dummy_glade():
	import gtk.glade
	return gtk.glade
	
def dummy_pygtkspellcheck():
	import gtkspellcheck
	return gtkspellcheck

def dummy_numpy():
	import numpy
	return numpy


def dummy_nltk():
	import nltk
	return nltk

def dummy_nltk_wordnet():
	from nltk.corpus import wordnet
	return wordnet

def dummy_nlt
