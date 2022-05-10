import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc

# now wait for the cyclic garbage collector to finish
gc.collect()


# Issue12, by Christian Tismer
# The issue is to let a __del__ popen
# the cycle, which would normally be
# detected and not collected.
#
# Here's the code, where a "function"
# is published in a module.  The
# function is actually a class with
# a useful __call__.  However the
# class has a __del__, which closes
# all references, so that the module
# then claims that the variable is
# not bound any longer.  The variable
# is actually still bound in the
# locals of the module.
globalvars = {}
def shutdown():
    global globalvars
    globalvars.clear()
atexit.register(shutdown)

class Wrecf:
    def __init__(self, name):
        self.name = name
        self.__dict__.update(module.__dict__)

    def __call__(self):
        global globalvars
        return globalvars[self.name]
