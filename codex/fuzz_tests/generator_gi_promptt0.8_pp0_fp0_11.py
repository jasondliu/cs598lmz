gi = (i for i in ())
# Test gi.gi_code
try: gi.gi_code
except AttributeError: pass
else: print('AttributeError expected')
# Check that gi.gi_code is None
try:
    if gi.gi_code is not None:
        print('gi.gi_code is not None')
except AttributeError as e:
    print('AttributeError: %s', e)

# Test gi.gi_frame
try: gi.gi_frame
except AttributeError: pass
else: print('AttributeError expected')
# Check that gi.gi_frame is None
try:
    if gi.gi_frame is not None:
        print('gi.gi_frame is not None')
except AttributeError as e:
    print('AttributeError: %s', e)

# Test gi.gi_running
try: gi.gi_running
except AttributeError: pass
else: print('AttributeError expected')
# Check that gi.gi_running is None
try:
    if gi.gi_running is not None:
        print('gi.gi_running is
