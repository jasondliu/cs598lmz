import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import os
import time
import json
import random
import re

import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s'
)

from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import pygtk
pygtk.require('2.0')
import gtk
import gobject

import pynotify

import gconf

import pycurl

import pyinotify

import gtkspell

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import gdata.gauth
import gdata.docs.service
import gdata.service

