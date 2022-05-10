gi = (i for i in ())
# Test gi.gi_code.co_name, which gives a function name
abc = (i for i in (1, 2, 3))

def foo(x):
	print(10)

bar = foo

print(abc.gi_code.co_name) # abc
print(bar.__code__.co_name) # foo

# Test gi_frame.f_code.co_argcount, which gives an integer of number of arguments
# of a function

def a(x, y, z):
	pass

print(bar.gi_frame.f_code.co_argcount) # 1
print(a.__code__.co_argcount) # 3
