gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame


class C:
	x = (i for i in ())


c = C()
code = c.x.gi_code
frame = c.x.gi_frame
if not isinstance(code, types.CodeType):
	raise TestFailed('gi_code not a code object')
if not isinstance(frame, types.FrameType):
	raise TestFailed('gi_frame not a frame object')
# Test that gi_frame and gi_code are usable as function arguments
frame = c.x.gi_frame
code = c.x.gi_code


def f(frame, code, x=c.x):
	locals = frame.f_locals
	if x is not frame.f_locals['x']:
		raise TestFailed('f_locals["x"] != frame.f_locals["x"]')


f(frame, code)
# Test that gen_close() works
def f1():
	yield 1
	yield 2
	yield 3
f = f1()
next
