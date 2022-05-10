from types import FunctionType
a = (x for x in [1])
b = [1]
print type(a)
print type(b)

def f():
    print "hello"

print type(f)

c = FunctionType(f.func_code, f.func_globals, f.func_name, f.func_defaults, f.func_closure)

print type(c)
print c.func_name
print c.func_code
print c.func_closure
print c.func_defaults
print c.func_globals
print c.func_dict
print c.__class__
print c.__class__.__dict__

c.func_name = "hello"
print c.func_name

c.func_code = "hello"
print c.func_code

c.func_closure = "hello"
print c.func_closure

c.func_defaults = "hello"
print c.func_defaults

c.func_globals = "hello"
print c.func_globals

c.func_dict = "hello"
print
