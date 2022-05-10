import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(r'/home/justin/Desktop/almadex/ACMIRI/test.db')

import pygments.lexers
import pygments.token

import index_model
import parse_c
import util

class indexer():
	def __init__(self, db=None):
		self.db = db
		self.events = []
		self.parent_events = []
		self.join_events = {}
		self.lock = threading.Lock();
		self.tokens_by_file = {}

	def autocomplete_scope(self, msg):
		scope = [i for i in msg if i not in [pygments.token.Literal, pygments.token.Operator, pygments.token.Punctuation]]
		if scope == []:
			return None
		scope = scope[-1]
		if scope.split('.')[-1] == '':
			scope = '.'.join(scope.split('.')[:-1])
		try:
		
