gi = (i for i in ())
# Test gi.gi_code is None for generators that have finished or that have
# not yet been started.
gi = (i for i in range(10))
code = gi.gi_code
next(gi)
next(gi)
next(gi)
next(gi)
next(gi)
next(gi)
next(gi)
next(gi)
next(gi)
next(gi)
try:
    next(gi)
except StopIteration:
    pass
try:
    gi.gi_code
except ValueError:
    pass
else:
    print("no ValueError when gi_code set to")
    print(gi.gi_code)
    print(code)

# Test gi.gi_frame is not None for generators that have been started.
gi = (i for i in range(10))
try:
    gi.gi_frame
except ValueError:
    print("ValueError when gi_frame set to", gi.gi_frame)
try:
    frame = gi.gi_frame
except ValueError:
    pass
else:
    print
