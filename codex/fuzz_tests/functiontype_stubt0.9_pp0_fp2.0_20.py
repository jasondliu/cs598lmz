from types import FunctionType
a = (x for x in [1])
b = (x for x in a)
c = (x for x in b)
type(c), type(a), type(a), len(dir(c))

c.gi_frame.f_locals
c.gi_frame.f_trace
next(c)
c.gi_frame.f_trace, c.gi_frame.f_trace is None
#c.gi_frame.f_exc_traceback, c.gi_frame.f_exc_traceback is None
c.gi_frame.f_exc_type, c.gi_frame.f_exc_type is None
c.close()

a = (x for x in [1])
a.gi_frame
def foo():
    yield
foo()
foo().gi_frame

#import cProfile   # cProfile.run 'python myscript.py' or cProfile.run('foo()', 'restats')
import pstats
pr = cProfile.Profile()
pr.enable()
# ... do something ...
pr.disable()
print 'Heads', pr.dump_stats()
