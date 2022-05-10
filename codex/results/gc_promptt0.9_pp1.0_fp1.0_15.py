import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect_generations():
for i in range(8):
    a = [None] * 100
    a = []
    gc.collect()

# Conditional flush of sys.stdout.  If <console>, no flush needed.
try:
    console = sys.stdout.isatty()
except AttributeError:
    console = 1

# Print the header
if not quiet:
    print 'Python', sys.version
    print 'Testing with flags:', gc.get_debug()
    print
    print '%5s %7s %5s %4s %7s  %s' % (
        'count', 'classes', 'size', 'type', 'format', 'repr')

# Print collection 0
if not quiet:
    print '%5d %7d %5d %4s %7s  %s...' % (
        0, # collection number
        len(gc.get_objects()), # number of objects
        asizeof(gc.garbage), # total size of objects
        '', # object type
        '', # str of
