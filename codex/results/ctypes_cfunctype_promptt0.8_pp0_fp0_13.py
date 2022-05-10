import ctypes
# Test ctypes.CFUNCTYPE()
try:
	@ctypes.CFUNCTYPE(None, None)
	def cf(): pass
except TypeError:
	print('SKIP')
	raise SystemExit

def cf():
	pass

print(ctypes.CFUNCTYPE(None, None))
print(ctypes.CFUNCTYPE(None, None)())
cf = ctypes.CFUNCTYPE(None, None)(cf)
print(cf)
cf()
