import ctypes
# Test ctypes.CFUNCTYPE cls

class C:
	def __init__(self):
		self.n = 0
	
	def callback(self, x):
		self.n += x
	
	def callback2(self, x):
		self.n *= x
	
	def callback3(self, x):
		self.n += 3
	
CB = ctypes.CFUNCTYPE(None, ctypes.c_uint)
a = C()
c = CB(a.callback)
c(1)
c(1)
print(a.n)
c2 = CB(a.callback2)
c2(2)
print(a.n)
c = CB(c.__call__) # !!!
print(isinstance(c, CB))
c(1)
print(a.n)

c3 = CB(a.callback3)
c3()
print(a.n)
