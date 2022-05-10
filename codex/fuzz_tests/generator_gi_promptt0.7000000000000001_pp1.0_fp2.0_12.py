gi = (i for i in ())
# Test gi.gi_code, gi.gi_frame, gi.gi_running, gi.gi_yieldfrom
class G:
    def __iter__(self):
        return self
    def __next__(self):
        return next(gi)

assert gi.gi_code is None
assert gi.gi_frame is None
assert gi.gi_running is True
assert gi.gi_yieldfrom is None

gi.send(None)
assert gi.gi_code is G.__next__.__code__
assert gi.gi_frame.f_code is G.__next__.__code__
assert gi.gi_running is False
assert gi.gi_yieldfrom is None

gi.send(1)
assert gi.gi_code is G.__next__.__code__
assert gi.gi_frame.f_code is G.__next__.__code__
assert gi.gi_running is False
assert gi.gi_yieldfrom is None

gi.send(2)
assert gi.gi_code
