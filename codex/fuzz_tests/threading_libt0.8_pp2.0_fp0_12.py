import threading
threading.stack_size(67108864)

# Standard library imports
import datetime
import sqlite3
import urllib2
import sys
import json

# Binary JSON library imports
import bjson

# This class is used to store jokes in a SQLite database
# It's very simple, but is highly optimized for fast storage and retrieval
#
# get_next() method fetches the next joke and returns it as a json string
# get_random() is similar, but fetches a random joke
class JokesDatabase(object):
    def __init__(self):
        self.conn = sqlite3.connect('jokes.db')
        self.conn.text_factory = str
        self.conn.execute('CREATE TABLE IF NOT EXISTS jokes (joke TEXT PRIMARY KEY, author TEXT, approved BOOLEAN, last_used DATETIME)')
        #self.conn.execute('CREATE TABLE IF NOT EXISTS jokes (id INTEGER PRIMARY KEY AUTOINCREMENT, joke TEXT,'
        #                         'author TEXT, array TEXT, approved BOO
