gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code.co_name)
# Test gi.gi_frame
print(gi.gi_frame.f_code.co_name)
# Test gi.gi_running
print(gi.gi_running)
gi.gi_running = False
print(gi.gi_running)
del gi.gi_running
try:
    gi.gi_running
except AttributeError:
    print("AttributeError")

# Test gi.gi_yieldfrom
def f():
    yield from [1, 2, 3]

gi = f()
print(gi.gi_yieldfrom)
gi.gi_yieldfrom = None
print(gi.gi_yieldfrom)
del gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    print("AttributeError")
