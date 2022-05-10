import gc, weakref, random
        
        # first create a dict to store weak references to the 2d_arrays,
        # to keep them alive until the last references to them go away
