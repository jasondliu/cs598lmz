import ctypes
import ctypes.util
import threading
import sqlite3
import urllib

#For the gui, update:
import subprocess

#For the gui
import shutil
import os



# Global variables
SQLITE_CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS
            DNSInfo(Name TEXT, Address TEXT, Type TEXT)'''
SQLITE_INSERT_ENTRY = '''INSERT INTO DNSInfo(Name, Address, Type)
            VALUES(?, ?, ?)'''
DNS_SERVER = ['8.8.8.8', '8.8.4.4']
SOCKET_LENGTH = 4096
SOCKET_TIMEOUT = 5 # seconds

#In order to communicate with the backend
#Regular expression to find what is the type of the query ->
#IP address or Name
#Expression for 4 integers separated by dots
IP_ADD = re.compile(
    r"""
    ^
    ([0-9]{1,3}\.){3,3}[0-9]{1,3}
    $
    """,
    re.VERBOSE
)


