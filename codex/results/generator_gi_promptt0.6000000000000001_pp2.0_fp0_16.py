gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print("SKIP")
    sys.exit()

# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    print("SKIP")
    sys.exit()

def g():
    yield 1
    yield 2

gi = g()
next(gi)
print(gi.gi_frame.f_lasti)
print(gi.gi_frame.f_lineno)

gi.gi_frame.f_lineno = 10
print(gi.gi_frame.f_lineno)

gi.gi_frame.f_lineno = 100
print(gi.gi_frame.f_lineno)
