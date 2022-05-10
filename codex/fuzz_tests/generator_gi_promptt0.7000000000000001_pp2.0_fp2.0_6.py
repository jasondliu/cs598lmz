gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print("SKIP")
    sys.exit()

# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    print("SKIP")
    sys.exit()

print(gi.gi_frame.f_code.co_filename)
