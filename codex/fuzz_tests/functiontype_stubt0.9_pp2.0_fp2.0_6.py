from types import FunctionType
a = (x for x in [1])
close = a.close
exit = a.close

close = (lambda: type(close))()
exit = (lambda: type(exit))()
del FunctionType
del a
#
del close
del open
del exit
try:
    import gc
    print(gc.get_stats()[0]['generations'])
except ImportError:
    print("gc module not available")
#
print "G1"  # make sure it's not optimized
