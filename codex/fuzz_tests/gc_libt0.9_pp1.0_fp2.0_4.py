import gc, weakref, random
        
        # first create a dict to store weak references to the 2d_arrays,
        # to keep them alive until the last references to them go away
        s = {}  # weak references go here
        # new make a dict of values we are cleaning which may have references
        # to 2d_arrays.  So delete this dict last, after we've weakly
        # referenced our 2d_arrays
        d = { 'not2d':Not2D(), 'list2d':List2D(), 'arr2d':Array2D() }

        # fill s with weak references to the 2d_arrays
        for key,value in d.items():
            s[key] = weakref.ref(value)

        del value

        # force collection so as to collect a few objects
        gc.collect(); gc.collect(); gc.collect()
        # get a count of objects
        nb_obj1 = len(gc.get_objects())
        self.assert_(nb_obj1 > 0) # make sure self.assert_ works
        
        # now throw
