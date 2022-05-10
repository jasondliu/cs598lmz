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

# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    print("SKIP")
    sys.exit()

# Test gi.gi_frame.f_lasti
try:
    gi.gi_frame.f_lasti
except AttributeError:
    print("SKIP")
    sys.exit()

# Test gi.gi_frame.f_trace
# try:
#     gi.gi_frame.f_trace
# except AttributeError:
#     print("SKIP")
#     sys.exit()

# Test gi.gi_frame.f_back
try:
    gi.gi_frame.f_back
except AttributeError:
    print("SKIP")
