import ctypes
ctypes.cast(0, ctypes.py_object)

import sys, atexit
sys.stdout.write('ordinary object destructors work for classes\n')

class puke(object):
	def __del__(self):
		sys.stdout.write('puke.__del__\n')

class vomit(object):
	def __del__(self):
		sys.stdout.write('vomit.__del__\n')

atexit.register(lambda : sys.stdout.write('atexit\n'))

