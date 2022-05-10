fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_frame.f_code
GlobalVar = fn.func_globals
PushGlobalVar = GlobalVar.__setitem__
DeleteGlobalVar = GlobalVar.__delitem__
GetGlobalVar = GlobalVar.__getitem__

def lastOut():
	"""Returns the last value output from a code section"""
	return ThisOut[-1]

def reOut(n):
	"""Returns the nth to last value output from a code section"""
	try:
		return ThisOut[-n-1]
	except IndexError:
		raise IndexError("Index out of range")

def lastIn(n):
	"""Returns the last value inputed into a code section"""
	return ThisIn[-1]

def reIn(n):
	"""Returns the nth to last value inputed into a code section"""
	try:
		return ThisIn[-n-1]
	except IndexError:
		raise IndexError("Index out of range")
