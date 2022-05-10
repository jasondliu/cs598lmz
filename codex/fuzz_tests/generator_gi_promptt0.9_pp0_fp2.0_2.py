gi = (i for i in ())
# Test gi.gi_code.co_name
fgi = (i() for i in ())
# Test gi.gi_code.co_name
agi = (i() for i in () for j in ())
agi.gi_code.co_name

# Test gi.gi_code.co_firstlineno
# Test gi.gi_code.co_name
def f42():
    g = (i for i in ())
    # Test gi.gi_code.co_firstlineno
    # Test gi.gi_code.co_name
def f43():
    # Test gi.gi_code.co_firstlineno
    # Test gi.gi_code.co_name
    g = (i for i in ())
    
def f44():
    # Test gi.gi_code.co_firstlineno
    gi = (i for i in ())
    return # Test gi.gi_code.co_firstlineno

def f45():
    # Test gi.gi_code.co_firstlineno
    [i for i in ()]
   
