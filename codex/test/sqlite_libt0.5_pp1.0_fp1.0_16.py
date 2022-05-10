import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import datetime
import sys
import subprocess
import socket
import json
import fcntl
import struct
import logging
import logging.handlers
import zipfile
import shutil
import psutil
import pwd
import grp
import traceback
import glob
import platform
import paho.mqtt.client as mqtt

# Global Variables
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address = '/dev/log')

formatter = logging.Formatter('%(module)s.%(funcName)s: %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

# Logger.
logger = logging.getLogger(__name__)

# Debugging.
debugging = False

# Debugging.
debugging2 = False

# Debugging.
debugging3 = False

# Debugging.
debugging4 = False


