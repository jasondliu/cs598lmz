fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_code)()
print(gi.gi_frame)
"""

"""
#print(sys.getrefcount(fn))
import sys

def test(a,b):
	global a
	a = 10
	print(a)

def main():
	a = 1
	b = 2
	test(a,b)
	print(a)
	print(sys.getrefcount(a))

if __name__ == "__main__":
	main()
"""

"""
import sys

print(sys.getrefcount(None))

"""
"""
def test():
	a = 1
	print(id(a))

test()

a = 2
print(id(a))
"""

"""
import sys

def test():
	a = 1
	print(sys.getrefcount(1))

test()
"""

"""
import sys

def test():
	a = 1
	print(sys.getrefcount(1))

test()
"""

