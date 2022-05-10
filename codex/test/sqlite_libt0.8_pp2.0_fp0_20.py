import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys

import Tkinter
from Tkinter import *
import ttk

import application.database as db
import application.tincan as tc
import application.tc_network as tc_net

from application.db_update import DBUpdate
from application.persistence import Persistence
from application.tincan_event import Tincan_event
from application.recommender import Recommender
from application.trend_detector import TrendDetector
from application.graph_controller import GraphController
from application.gui_manager import GUIManager

def main():
    # load required libraries
    ctypes.CDLL(ctypes.util.find_library('usb-1.0'))
    ctypes.CDLL(ctypes.util.find_library('usb'))
    ctypes.CDLL(ctypes.util.find_library('udev'))

    # begin setup for TinCan
    tc_net.init()
    tc.init()
    tc.set_device_event_handler(on_tincan_event)

    # create required objects

