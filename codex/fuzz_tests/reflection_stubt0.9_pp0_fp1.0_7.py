fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    marshal.dumps(fn.__code__)
except TypeError:
    pass
else:
    print("dumps(fn.__code__) wrong exception")

d = {'__import__': lambda x: 42}
try:
    exec("__import__('sys')", d)
except TypeError:
    pass
else:
    print('No exception for exec() calling __import__()')

try:
    eval('__import__("sys")')
except TypeError:
    pass
else:
    print('No exception for eval() calling __import__()')

# eval called from __code__ is allowed
d = {"__code__": compile("__import__('sys')", '<code>', 'exec')}
try:
    exec(d["__code__"])
except SystemExit:
    pass

# ditto for exec
# "__code__" is allowed (type check happens later)
d = {"__code__": compile("__import__('sys')", '<code>', 'exec')}
try:

