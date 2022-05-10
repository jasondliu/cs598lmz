gi = (i for i in ())
# Test gi.gi_code
#, gi.gi_frame
#, gi.gi_running
#, gi.gi_yieldfrom
gi.gi_code = None
# Test gi.gi_frame
#, gi.gi_running
#, gi.gi_yieldfrom
gi.gi_frame = None
# Test gi.gi_running
#, gi.gi_yieldfrom
gi.gi_running = True
# Test gi.gi_yieldfrom
gi.gi_yieldfrom = None

# Test for sys.getprofile()
#sys.getprofile()

# Test for sys.getrefcount()
#sys.getrefcount(1)

# Test for sys.getsizeof()
#sys.getsizeof(1)

# Test for sys.setcheckinterval()
#sys.setcheckinterval(1)

# Test for sys.setprofile()
#sys.setprofile(None)

# Test for sys.setrecursionlimit()
#sys.setrecursionlimit(1)

# Test for sys.set
