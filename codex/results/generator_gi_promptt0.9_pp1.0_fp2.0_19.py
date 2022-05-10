gi = (i for i in ())
# Test gi.gi_code
gi.gi_code

# Test gi.gi_frame
# The frame is explicitly null, because frame is not available at definition
# time except for generator functions defined in the top level of a module.
# Otherwise, a frame is  only available at run time and should not be
# stored -- instead, a null pointer is stored until the generator is
# executed; subsequently, the frame is fetched from the generator object.
gi.gi_frame is None

# Test PyGen_Check and PyGen_CheckExact
PyGen_Check(gi)
PyGen_CheckExact(gi)

# Test gi.gi_running
gi.gi_running
