gi = (i for i in ())
# Test gi.gi_code

def f():
    pass

f.__code__.co_flags = 0x400

gi = (i for i in ())

try:
    gi.gi_code
except ValueError as e:
    print(e)

# Test gi.gi_frame

def f():
    pass

f.__code__.co_flags = 0x400

gi = (i for i in ())

try:
    gi.gi_frame
except ValueError as e:
    print(e)
