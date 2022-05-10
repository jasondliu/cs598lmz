import gc, weakref


class GcTester(object):
    def __init__(self, verbose=1):
        self.verbose = verbose
        self.objects = []

    def add(self, object):
        """Add an object to the list of objects tracked by this tester."""
        self.objects.append(weakref.ref(object))
        return object

    def run(self, func, args, kwargs):
        """Run a given function and track objects that are allocated while
        running it.  Return the result of the function call."""
        # Add the objects that are already in the list of tracked objects
        # before running the function.
        gc.collect()
        objects_before = {}
        for o in self.objects:
            o = o()
            if o is not None:
                objects_before[id(o)] = o

        # Run the function.
        result = func(*args, **kwargs)

        # Add the objects that are in the list of tracked objects after
        # running the function.
        gc.collect()
        objects_after
