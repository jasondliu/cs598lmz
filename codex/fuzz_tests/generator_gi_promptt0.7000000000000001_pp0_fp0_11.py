gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print("SKIP")
    raise SystemExit

for x in gi:
    print("unreachable")
print(gi.gi_frame.f_lasti)
