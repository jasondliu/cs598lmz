import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import subprocess
import time
import re

# Open database
conn = sqlite3.connect('/home/pi/Documents/Python/weatherdb.db')
c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE weather (timestamp text, temp real, humidity real)''')

# Insert a row of data
# c.execute("INSERT INTO weather VALUES ('2018-02-17 13:40:00', 22.0, 43.0)")

# Save (commit) the changes
# conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
# conn.close()

# libc = ctypes.CDLL(ctypes.util.find_library('c'))
# res_init = libc.__res_init
# res_init()

# def run_cmd(cmd):
#     p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE
