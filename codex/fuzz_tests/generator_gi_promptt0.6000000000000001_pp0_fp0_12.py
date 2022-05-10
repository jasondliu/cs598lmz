gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print("SKIP")
    raise SystemExit

def f():
    yield 1

fg = f()

# Check gi_code is a code object
print(type(fg.gi_code))
print(fg.gi_code.co_name)

# Check gi_frame is a frame object
print(type(fg.gi_frame))
print(fg.gi_frame.f_code.co_name)

# Check gi_running is False
print(fg.gi_running)

# Check gi_running is True
next(fg)
print(fg.gi_running)

# Check gi_running is False
next(fg)
print(fg.gi_running)

# Check gi_yieldfrom
def f2():
    yield from f()

fg = f2()
next(fg)
print(fg.gi_yieldfrom)

# Check gi_running is False
next(fg)
print(fg.gi_running)
