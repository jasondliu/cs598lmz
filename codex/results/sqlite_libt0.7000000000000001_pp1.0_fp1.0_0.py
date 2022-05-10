import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime
import os
import sys
import logging
from logging.handlers import RotatingFileHandler
import importlib
import inspect
import re
from serial import Serial
import subprocess
from subprocess import call
from subprocess import Popen
import json
import urllib2
import RPi.GPIO as GPIO

from . import config
from . import constants as const
from . import utils
from . import log
from . import db
from . import sensors
from . import actuators
from . import network
from . import file
from . import _version

LOGGER = logging.getLogger(__name__)


def main():
    """
    Main entry point.
    """
    print("")
    print("****************************************")
    print("*     Welcome to bemoss v." + str(_version.__version__) + "      *")
    print("*   This is a beta version.            *")
    print("*   Report any issues at,              *")
    print("*   http://github.com/bemoss/BEMOSS_os *
