import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage

# In debug mode, collect is a no-op
# and returns None
gc.collect()
gc.collect()

# In debug mode, garbage is a list of weak
# references that have been collected
# since the last debug-mode collect
gc.garbage

# Clear debug mode and run a collect
gc.set_debug(0)
gc.collect()

# Now gc.garbage is empty
gc.garbage

# Do a collect in debug mode again
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.collect()

# Now gc.garbage is a list of two weak
# references to the temporary tuple
# from the first gc.collect call
gc.garbage

# Clear debug mode and run a collect again
gc.set_debug(0)
gc.collect()

# Now gc.garbage is empty again
gc.garbage
 
#################
# test_gc.py
# Copyright (C) 2005-2012 the ChiliProject Team
#
# This program is free software; you can
