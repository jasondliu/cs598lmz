gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
print("gi.gi_frame: {}".format(gi.gi_frame))
print("gi.gi_frame.f_code: {}".format(gi.gi_frame.f_code))
# Test gi.gi_frame.clear (should fail)
#gi.gi_frame.clear()
# Test gi.gi_frame.clear_free_list (should fail)
#gi.gi_frame.clear_free_list()
# Test gi.gi_frame.__class__
print("gi.gi_frame.__class__: {}".format(gi.gi_frame.__class__))
# Test gi.gi_frame.__delattr__
#gi.gi_frame.__delattr__("")
# Test gi.gi_frame.__dir__
print("gi.gi_frame.__dir__(): {}".format(dir(gi.gi_frame)))
# Test gi.gi_frame.__doc__
print("gi.gi_frame.__doc__: {}".format(
