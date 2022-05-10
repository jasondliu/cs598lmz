gi = (i for i in ())
# Test gi.gi_code.co_flags parameter
assert gi.gi_code.co_flags == 0x00003
gi = (i for i in ())
# Various attributes of gi_code.co_flags
# name code_object.co_flags #
assert code_object.co_flags == 0x0003
# name code_object.co_flags #
assert code_object.co_flags == 0x0003
# Generators raising StopIteration
def f():
    yield
    yield
res = f()
# iterator attributes
assert res.gi_code == f.func_code
# Next is available for __iter__ method.
assert not hasattr(f(), "next")
# StopIteration is raised if next() is called
assert hasattr(f(), "send")
# iterator attributes
assert res.gi_frame is not None
assert isinstance(res.gi_frame, types.FrameType)

# StopIteration is raised if next() is called
# StopIteration is raised if next() is called
# StopIteration is raised if next() is called
assert res.next() == 0
assert
