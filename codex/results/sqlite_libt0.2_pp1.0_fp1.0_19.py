import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import subprocess
import signal
import re

#
# This is the main class for the program.
#
class Main:
    #
    # This is the constructor for the class.
    #
    def __init__(self):
        #
        # Initialize the class.
        #
        self.init()
        #
        # Start the program.
        #
        self.start()
        #
        # Exit the program.
        #
        self.exit()
    #
    # This is the init function for the class.
    #
    def init(self):
        #
        # Set the name of the program.
        #
        self.name = "sensor"
        #
        # Set the version of the program.
        #
        self.version = "1.0.0"
        #
        # Set the author of the program.
        #
        self.author = "Michael Treanor"
        #
        # Set the copyright of the program.
        #
        self.copyright = "
