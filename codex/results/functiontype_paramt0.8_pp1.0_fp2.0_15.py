from types import FunctionType
list(FunctionType(fib, globals(), "fib"))
list(map(fib, range(10)))

import logging
logging.basicConfig(level=logging.DEBUG)
def log(message, when=None):
    if when is None:
        when = time.time()
    logging.info("%s: %s" % (when, message))
log("Hi there!")

print("""You can use optional key-word arguments to extend functions in safe ways.
For example, it is safe to add a new key-word argument to a function because
code that does not provide the new argument will simply get the default value.


def decode(data, default={}):
    try:
        return json.load(data)
    except ValueError:
        return default
""")
foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print("foo and bar are the same object? ", foo is bar)

print("""
Here's a new version that passes the optional argument by keyword so that
a default dictionary is not
