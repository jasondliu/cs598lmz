import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
from xml.etree.ElementTree import ElementTree, Element, SubElement
from xml.etree import ElementTree
from xml.dom import minidom
import time
from datetime import datetime, timedelta

from . import logging



LIBMTP_DATA_TYPE_FOLDER = LIBMTP_FILETYPE_FOLDER
LIBMTP_DATA_TYPE_AUDIO = LIBMTP_FILETYPE_AUDIO
LIBMTP_DATA_TYPE_VIDEO = LIBMTP_FILETYPE_VIDEO
LIBMTP_DATA_TYPE_IMAGE = LIBMTP_FILETYPE_IMAGE
LIBMTP_DATA_TYPE_PLAYLIST = LIBMTP_FILETYPE_PLAYLIST
LIBMTP_DATA_TYPE_TEXT = LIBMTP_FILETYPE_TEXT
LIBMTP_DATA_TYPE_FIRMWARE = LIBMTP_FILETYPE_FIRMWARE
LIBMTP_DATA_TYPE_UNKNOWN = LIBMTP_FILETYPE_UNKNOWN
LIBMTP_DATA_TYPE_EXECUTABLE = LIBMTP_FILETYPE_EX
