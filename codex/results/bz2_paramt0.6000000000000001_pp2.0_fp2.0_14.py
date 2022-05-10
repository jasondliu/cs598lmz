from bz2 import BZ2Decompressor
BZ2Decompressor.__module__ = 'bz2'

import imp, sys, os, time, struct, select, socket, re, random, string
import traceback, gc, hmac, tempfile, errno, getopt, subprocess, signal
import base64, zlib, ssl, urllib, urllib2, httplib, urlparse

try:
	from hashlib import md5
except ImportError:
	from md5 import md5

try:
	import cPickle as pickle
except ImportError:
	import pickle

try:
	import json
except ImportError:
	import simplejson as json

try:
	import Crypto.Cipher.AES
except ImportError:
	if os.name == 'nt':
		sys.stderr.write('Crypto.Cipher.AES is not installed, which is required on Windows\n')
		sys.exit(1)

try:
	import Crypto.PublicKey.RSA as RSA
except ImportError:
	if os.name == 'nt':
		sys.st
