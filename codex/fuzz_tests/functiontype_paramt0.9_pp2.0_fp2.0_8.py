from types import FunctionType
list(FunctionType() for _ in range(100))

# So why doesn't the first line create GC pressure?  linecache.getlines
# probably uses getline's return value somewhere.
linecache.getlines('stdlib_logging_getlines_q.py')

def closure_creates_ref():
    i = 0
    def getline(l):
        nonlocal i
        i += 1
        return l
    linecache.getlines('.', getline)
    return  i

# Now we see a lot of GC load.
data = linecache.getlines('..')

# Why this many? linecache uses second argument only if first is list.
# The next test will pass with closure_creates_ref instead.
assert closure_creates_ref() != len(data), len(data)

# Because linecache keeps a cache object, we get rid of the references, but
# they're not reclaimed:
del data
del getline

# Now the linecache cache is cleaned.
import gc; gc.collect()


# Test for linecache.updatecache.  This
