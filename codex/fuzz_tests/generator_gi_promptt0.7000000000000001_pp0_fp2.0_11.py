gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print('AttributeError not raised')
# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    print('AttributeError not raised')
# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    pass
else:
    print('AttributeError not raised')
# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    pass
else:
    print('AttributeError not raised')

# Test ti.ti_frame
try:
    ti.ti_frame
except AttributeError:
    pass
else:
    print('AttributeError not raised')
# Test ti.ti_lasti
try:
    ti.ti_lasti
except AttributeError:
    pass
else:
    print('AttributeError not raised')
# Test ti.ti_block
try:
    ti.
