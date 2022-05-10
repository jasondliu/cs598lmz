import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

# Import ProgressBar
#from progressbar import *
#import time

# Test ProgressBar
#pbar = ProgressBar()
#for i in pbar(range(100)):
#    time.sleep(0.02)

# test sqlite3
#import sqlite3
#conn = sqlite3.connect('hello.sqlite')
#cur = conn.cursor()
#cur.execute('DROP TABLE IF EXISTS Counts')
#cur.execute('''
#CREATE TABLE Counts (org TEXT, count INTEGER)''')
#fname = input('Enter file name: ')
#if (len(fname) < 1): fname = 'mbox.txt'
#fh = open(fname)
#for line in fh:
#    if not line.startswith('From: '): continue
#    pieces = line.split()
#    email = pieces[1]
#    org = email.split('@')[1]
#    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
