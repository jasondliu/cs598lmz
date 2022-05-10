import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import subprocess
import shutil
import re

from lib.common import helpers

class Stager:

    def __init__(self, mainMenu, params=[]):

        self.info = {
            'Name': 'Launcher',

            'Author': ['@harmj0y'],

            'Description': ("Launches a payload listener (multi/handler) or "
                            "migrates to a specified process."),

            'Comments': [
                ''
            ]
        }

        # any options needed by the stager, settable during runtime
