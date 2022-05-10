import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
	return None

def test_return_none():
	assert fun() is None

def test_return_true():
	@FUNTYPE
	def fun():
		return True
	assert fun() is True

def test_return_false():
	@FUNTYPE
	def fun():
		return False
	assert fun() is False

def test_return_int():
	@FUNTYPE
	def fun():
		return 42
	assert fun() == 42

def test_return_float():
	@FUNTYPE
	def fun():
		return 3.14
	assert fun() == 3.14

def test_return_str():
	@FUNTYPE
	def fun():
		return "Hello"
	assert fun() == "Hello"

def test_return_unicode():
	@FUNTYPE
	def fun():
		return u"Hello"
	assert fun() == u"Hello"

def test_return_tuple():
	@FUNTYPE
	def fun():
		return (1, 2, 3)
	assert fun
