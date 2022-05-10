import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import re
import datetime
import math
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.session = gps.gps("localhost", "2947")
        self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
        self.current_value = None

    def get_current_value(self):
        return self.current_value

    def run(self):
        try:
            while True:
                self.current_value = self.session.next()
                # print self.current_value
                # Wait for a 'TPV' report and display the current time
                # To see all report data, uncomment the line below
                # print gpsd.next()
        except StopIteration:
            pass

