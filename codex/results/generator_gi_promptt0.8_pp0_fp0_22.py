gi = (i for i in ())
# Test gi.gi_code.co_flags
def func_gi():
    return (i for i in ())
gi = func_gi()
# Test gi.gi_code.co_flags
gi = (i for i in range(0))
# Test gi.gi_code.co_flags
gi = (i for i in [])
# Test gi.gi_code.co_flags
gi = (i for i in {})
# Test gi.gi_code.co_flags
gi = (i for i in 0)
# Test gi.gi_code.co_flags
gi = (i for i in 1)

# Test code.co_flags
def func_code():
    (i for i in ())
def func_code():
    (i for i in range(0))
def func_code():
    (i for i in [])
def func_code():
    (i for i in {})
def func_code():
    (i for i in 0)
def func_code():
    (i for i in 1)

# Test co_code
# Test co_
