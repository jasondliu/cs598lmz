import ctypes
import ctypes.util
import threading
import sqlite3
import os, sys
import logging
import subprocess
import pwd
import json

from . import lib
from . import utils

def init_logging():
	logging.basicConfig(level=logging.INFO, format=utils.LOG_FORMAT_STR)

def init_db(dbname, config):
	with sqlite3.connect(dbname) as db:
		c = db.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER NOT NULL,
													   username TEXT NOT NULL,
													   password TEXT NOT NULL,
													   PRIMARY KEY (id),
													   UNIQUE (username))""")
