import ctypes
import ctypes.util
import threading
import sqlite3
import sqlite3 as lite
import sys
import time
import json
import urllib2
import urlparse
import optparse

from sqlite3 import Error

class history:
    def __init__(self):
        print("class history")
        conn = sqlite3.connect("firefox.db")
        cursor = conn.execute("select url from moz_places where url like 'http%' and last_visit_date between 1526851211 and 1526851212")
        
        for row in cursor:
            print "ok"



def main():
    history()

main()
