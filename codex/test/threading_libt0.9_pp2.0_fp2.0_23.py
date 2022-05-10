import threading
threading.stack_size(2**27)
import sys
import glob
sys.path.append(r'./resources/')
from vram_checker import VRAMChecker
from forecast_list_checker import ForecastListChecker
from file_garbage_cleaner import FileGarbageCleaner
from file_garbage_cleaner import get_font
from pathlib import Path
from datetime import datetime
from threading import Timer
from PIL import ImageTk
from git import Repo
from functools import partial
from tkinter import *
from tkinter.font import Font
from tkmessagebox import showerror
from tkinter import ttk
from tkinter.ttk import *
from ecmwfapi import ECMWFDataServer
from netCDF4 import Dataset
from cachetools import LRUCache
from random import choice
import netCDF4
import tkinter as tk
import subprocess
import json, os, base64
from os.path import expanduser
from calendar import monthrange
from datetime import timedelta
