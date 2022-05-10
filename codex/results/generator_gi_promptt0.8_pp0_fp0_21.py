gi = (i for i in ())
# Test gi.gi_code.co_filename is not None.
assert gi.gi_code.co_filename is not None

# Test gi.gi_frame's back reference to gi.
assert gi.gi_frame.f_back == gi
try:
    next(gi)
except StopIteration:
    pass
else:
    assert False, 'expected exception'

# Test gi.gi_frame's back reference to gi.
assert gi.gi_frame.f_back == gi



# Test GeneratorExit bubbling - basically a copy of test_exc_handling.py
def _step1():
    yield 1

class Exception2(Exception):
    pass

def _step2():
    try:
        yield 2
    except Exception2:
        yield 3
    else:
        yield 4
    finally:
        yield 5

def _step3():
    yield 6
    try:
        yield 7
    except:
        yield 8
    else:
        yield 9
    finally:
        yield 10

def _step4():
    try:
