fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
code = fn.__code__
getcode = code.__code__
print(getsource(getcode))
sys.exit(0)

o = Open(fn.__code__)
print(o)
print(getsource(fn.__code__))
print(getsource(o.__code__))

syscall = lambda: 0
print(getsource(syscall.__code__))
tainted_object = syscall
print(getsource(tainted_object.__code__))

sys.exit(0)


"""
def getcode(self, object, default=None):
    """Return the code object associated with the object.

    If the object does not have a code object
    then the *default* value is returned.

    """
    try:
        return object.__code__
    except AttributeError:
        return default
"""

"""
code(argcount, nlocals, stacksize, flags, codestring, constants, names,
      varnames, filename, name, firstlineno, lnotab, freevars, cell
