gi = (i for i in ())
# Test gi.gi_code
issubclass(type(gi.gi_code), types.CodeType)
# Test gi.gi_frame
issubclass(type(gi.gi_frame), types.FrameType)
n = 0
for i in gi:
    n += 1
    if n > 100:
        break
print(n)

# Test gi.gi_yieldfrom
def gen():
    yield from range(10)

gi = gen()
assert next(gi) == 0
assert next(gi) == 1
# Test gi.gi_yieldfrom
gi = (i for i in range(10))
assert next(gi) == 0
assert next(gi) == 1
gi = (i for i in range(10))
assert next(gi) == 0
assert next(gi) == 1

# Test gi_running
gi = ((yield) for i in (1, 2, 3))
try:
    next(gi)
except StopIteration:
    pass
assert gi.gi_running is False

# Test gi_frame.f_lasti
