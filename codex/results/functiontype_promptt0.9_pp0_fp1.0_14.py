import types
# Test types.FunctionType, types.UnboundMethodType, and
# types.ClassMethodType
import unittest

class A(object):
	def f(self):
		print "hello world"

def g():
	print "hello world"

a=A()

class TypeTest(unittest.TestCase):
	def xtestUnboundMethod(self):
		# Check that this is what we intended to test.
		self.failUnless(getattr(A, "f") is A.f)

		# In the new-style class model, (un)bound methods are gone
		#self.failUnless(type(a.f) is types.UnboundMethodType)
		self.failUnless(type(a.f) is types.MethodType)
		self.failIf(type(a.f) is types.FunctionType)
		self.failIf(type(a.f) is types.BuiltinFunctionType)
		self.failIf(type(a.f) is types.BuiltinMethodType)
		self.failIf(
