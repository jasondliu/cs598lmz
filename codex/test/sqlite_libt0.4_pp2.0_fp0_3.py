import ctypes
import ctypes.util
import threading
import sqlite3
import time
import uuid
import os
import sys
import re
import subprocess
import datetime
import shutil
import argparse
import json
import random
import string
import hashlib
import base64
import tempfile

# this is the default path to the sqlite database
# it is recommended to change this to a different path
# on a different filesystem
# you can use the -d option to change the location of the database
DB_PATH = os.path.join(os.path.expanduser("~"), ".pytbull", "pytbull.db")

# this is the default path to the log file
# it is recommended to change this to a different path
# on a different filesystem
# you can use the -l option to change the location of the log file
LOG_PATH = os.path.join(os.path.expanduser("~"), ".pytbull", "pytbull.log")

# this is the default path to the config file
# it is recommended to change this to a different path
# on a different filesystem
# you can use the -c option to change the
