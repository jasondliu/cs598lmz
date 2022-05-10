import ctypes
import ctypes.util
import threading
import sqlite3
import random
import string
import base64
import subprocess

curr_version = 1

work_folder = "./"
work_db = work_folder+"Skynet.db"

connection = sqlite3.connect(work_db)
