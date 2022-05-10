gi = (i for i in ())
# Test gi.gi_code for an uninitialized generator

def gen_uninit():
    pass

gi = gen_uninit()
print("gi_code", gi.gi_code)
print("gi_code.co_name", gi.gi_code.co_name)
if "gi_frame" in dir(gi):
    print("gi_frame", gi.gi_frame)
elif "gi_frame" in gi.__dict__:
    print("gi_frame", gi.__dict__["gi_frame"])

try:
    gi_frame = gi.gi_frame
except AttributeError:
    resolved_frame = None
else:
    resolved_frame = gi_frame

try:
    resolved_frame.f_code.co_name
except AttributeError:
    print("resolved_frame.f_code.co_name", "<unresolved>")
else:
    print("resolved_frame.f_code.co_name", resolved_frame.f_code.co_name)

try:
    gi.gi
