from types import FunctionType
a = (x for x in [1])
print type(a)
print type((lambda x: x))
print type(sum)

b = FunctionType(a, b, c)

# Create a function from a code object using new.function().


import sys
def test():
	print "in test"
	sys._getframe(1)

CO_GENERATOR = 0x0020
def generator(code, globals):
	g = (c() for c in [])
	g.gi_code = code
	g.gi_frame = sys._getframe(1)
	return g

def test2():
	print "in test2"
	a = (x for x in [1])	
	print type(a)
	print a.gi_frame
	print test2.func_code

def Main():
	test2()


if __name__ == '__main__':
	Main()
