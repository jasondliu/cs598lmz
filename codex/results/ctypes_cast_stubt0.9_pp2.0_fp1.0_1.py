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

import __builtin__
__builtin__.x = x = puke()
del x
try:
	__builtin__.x = x = vomit()
	del x
except TypeError:
	sys.stdout.write('oops, vomit isnt destructible\n')

raise Exception
"""

import sys
if "create_refcycle" not in sys.builtin_module_names:
	if sys.version < "2.4":
		skip("cannot test, Py_LIMITED_API too old")
