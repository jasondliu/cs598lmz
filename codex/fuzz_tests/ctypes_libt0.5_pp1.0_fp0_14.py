import ctypes
ctypes.windll.user32.SetProcessDPIAware()
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from os import listdir
from os.path import isfile, join
import time
import threading
from threading import Thread
import io
from io import BytesIO
import requests
from requests import get
from urllib.request import urlopen
import datetime
import sys
from datetime import date
from sys import platform
from bs4 import BeautifulSoup
import re
from re import search
import json
from json import dumps
from tkinter import messagebox
import webbrowser
import warnings
from warnings import simplefilter
import copy
from copy import deepcopy
import pickle
from pickle import loads
from pickle import dumps
import pyautogui
from pyautogui import position
from pyautogui import moveTo
from pyautogui import click
from pyautogui import size
from pyautogui import hotkey
from pyautogui import press
from pyautogui import typewrite
from pyaut
