import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import time
import os.path
import sys

# Set up the sqlite connection.
if os.path.exists('/usr/share/anki/'):
  base = '/usr/share/anki/'
elif os.path.exists('/usr/local/share/anki/'):
  base = '/usr/local/share/anki/'
else:
  raise Exception("Cannot locate Anki folder.")

if not len(sys.argv) == 2:
  print("USAGE: python %s <database>") % (sys.argv[0])
  sys.exit()

db = sys.argv[1]

with open("%sweb/templates/progress.html" % (base), 'r') as f:
  progress = f.read().replace("\n", "").replace("'", "\\'").replace("\"", "\\\"")

# Initialize the database.
conn = sqlite3.connect(db)
c = conn.cursor()

# Make sure we use the
