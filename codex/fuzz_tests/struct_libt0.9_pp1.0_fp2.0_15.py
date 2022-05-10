import _struct
import _tty
import array
import bin
import cmath
import cPickle
import fcntl
import gettext
import grp
import itertools
import md5
import operator
import os
import random 
import readline
import select
import sha 
import socket
import string 
import struct
import termios
import time
import unicodedata
import user
import weakref

import select
from cPickle import Pickler
import sys
import gc
	
def displayhook(obj):
	'''
	custom displayhook
	used in place of the builtin displayhook
	and just to illustrate how to do it
	'''
	#	print "in displayhook"
	#	print obj
	#
	#	#
	#	# this is how you might do things if you
	#	# are just interested in builtin types
	#	#
	
	#	if obj is None:return 'NONE'
	#	if isinstance(obj, str):return 'STRING: %s' % obj
	#	if isinstance
