gi = (i for i in ())
# Test gi.gi_code is not None

class G:
    def __init__(self):
        self.gi = (i for i in ())

g = G()
# Test g.gi.gi_code is not None

# Test that gi_frame is not None
def f():
    gi = (i for i in ())
    return gi

gi = f()
# Test gi.gi_frame is not None

def f():
    gi = (i for i in ())
    return gi

gi = f()
# Test gi.gi_frame is not None

# Test that gi_frame is not None
def f():
    gi = (i for i in ())
    return gi

gi = f()
# Test gi.gi_frame is not None

# Test that gi_frame is not None
def f():
    gi = (i for i in ())
    return gi

gi = f()
# Test gi.gi_frame is not None

# Test that gi_frame is not None
def f():
   
