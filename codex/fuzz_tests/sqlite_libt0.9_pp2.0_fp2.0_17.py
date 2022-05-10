import ctypes
import ctypes.util
import threading
import sqlite3
import os
import os.path
import platform
import json
import getpass
import urllib.request, urllib.error, urllib.parse
import configparser
import datetime
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

if platform.system() == "Windows":
    libc = ctypes.CDLL(ctypes.util.find_library('msvcrt'))
else:
    libc = ctypes.CDLL(ctypes.util.find_library('c'))

try:
    raw_input
except NameError:
    raw_input = input

global get_details
global Address1
global Address2
global address_privkey
global config
global p

def history_index(index_num,index_integer):
	'''
	Creates a unique filename based on a number provided.
	'''
	global p
	history_insert = p.history_insert
	history_socket = p.history_socket
	history_login = p.history_login
	history
