import gc, weakref
import dis, types, sys
from magnum import get_hooks, set_hooks
from magnum.core import vec, loop_hierarchy, loop_body
# These contain potential references to different bits of program state
# we need to get rid of when switching tests.
# TODO: move this into actual framework.
class cls:
    def __init__(self): pass
class tup:
    def __new__(self): return ()
class instance(object):
    def __new__(self): return cls()

class test_import_gen(object):
    # shadowing of names does not require stack frames,
    # so generator-based classes don't need the overhead
    # of large stacks.
    stack_size = 2 

    def pgen(self, program, argv=()):
        return VM(program, argv, self.stack_size)
    def cgen(self, args):
        return Compiler(self.code, args, self.stack_size)

    txt = """
print "running tests after import"
def a(x):
