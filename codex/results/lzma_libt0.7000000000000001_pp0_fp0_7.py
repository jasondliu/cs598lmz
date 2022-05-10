import lzma
lzma.__version__

import PySimpleGUI as sg
from PySimpleGUI import Text, Output
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *

from time import sleep
from os import path
from os import getcwd
from os.path import exists
from os.path import join
from os.path import basename
from os import listdir
from os import mkdir

from threading import Thread
from threading import RLock

import json
from PIL import ImageTk, Image
from shutil import copyfileobj

from urllib.request import urlopen
from urllib.parse import quote
from urllib.request import Request
from urllib.request import urlretrieve
from urllib.error import HTTPError
from urllib.error import URLError

from bs4 import BeautifulSoup

from ctypes import windll
from ctypes import wintypes
from ctypes import byref
from ctypes import create_unicode_buffer
from ctypes import c_void_p
from ctypes
