gi = (i for i in ())
# Test gi.gi_code
# Test gi.gi_frame
# Test gi.gi_running
# Test gi.gi_name
# Test gi.gi_frame.f_lasti


class C:
    def bar(self):
        pass

    def __iter__(self):
        i = 0
        yield i

        i = 1
        yield i

        i = 2
        yield i
        return

# Test gi.gi_frame.f_locals

g = C()
it = g.__iter__()
# Test getlocal
# Test getlocal
# Test getlocal
# Test getlocal
# Test getlocal
next(it)
# Test getlocal
# Test getlocal
# Test getlocal
# Test getlocal
# Test getlocal
next(it)
# Test getlocal
# Test getlocal
# Test getlocals
# Test getlocals
# Test getlocal
# Test getlocals
try:
    next(it)
except StopIteration:
    pass
# Test getlocal
# Test getlocal
# Test getlocals
# Test
