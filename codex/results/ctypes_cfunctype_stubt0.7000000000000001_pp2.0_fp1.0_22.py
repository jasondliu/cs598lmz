import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
	print "hi"

@FUNTYPE
def fun2(x):
	print x
	return x

@FUNTYPE
def fun3(x, y):
	print x, y
	return x + y

def fun4(x):
	print x
	return x


def blah():
	print "blah"

class MyObject(object):
	def __init__(self):
		pass

	def func(self):
		print "hi"
		return 1

def func(x):
	print x
	return x

class Test(unittest.TestCase):
	def test_1(self):
		fun()
		fun = FuncObject(lambda: 1)
		assert fun() == 1

	def test_2(self):
		fun2(5)
		fun2 = FuncObject(lambda x: x)
		assert fun2(5) == 5

	def test_3(self):
		fun3(5, 6)
		fun3 = FuncObject(lambda x
