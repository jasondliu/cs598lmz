from types import FunctionType
list(FunctionType(list, []).__globals__)

# the __globals__ attribute of the builtins module
import builtins
builtins.__globals__

# the __globals__ attribute of the modules (not every attribute
# of a module is also global though)
import sys
sys.__globals__


# the __dict__ attribute of a class (not every attribute is
# global either)
class Foo:
	def __init__(self):
		self.bar = 42
Foo.__dict__

# the __dict__ attribute of objects (not every attribute is global)
class Ex(Exception):
	def __init__(self):
		self.foo = len("hello")
w = Ex()
w.__dict__

# the __globals__ attributes of functions
# NOTE: a nonlocal global variable is NOT reported!
def foo():
	g1 = 0
	def bar():
		global g2
		g3, g4 = 42, 42
		print(bar.__globals__)
	bar()

