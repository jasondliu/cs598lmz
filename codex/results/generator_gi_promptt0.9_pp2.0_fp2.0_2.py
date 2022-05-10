gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame with generator object
gen = gen_gi
try:
    gen.gi_code
    gen.gi_frame
except AttributeError:
    print("SKIP")
    raise SystemExit
print(gen.gi_code)
print(gen.gi_frame)
