fn = lambda: None
# Test fn.__code__/fn.co_filename/fn.co_name on Python 3.4+.
try:
    fn.__code__
except AttributeError:
    pass
else:
    # The following code hacks into the function to set the
    # __code__ and __name__ fields to make them look like
    # the code block we want to be tracing.  Code copied
    # from the Python stdlib, inspect.py.

    def currentframe():
        """Return the frame object for the caller's stack frame."""
        try:
            raise Exception
        except:
            return sys.exc_info()[2].tb_frame.f_back

    def getinnerframes(etb, context=1):
        """Get a list of records for a traceback's frame and all lower frames.

        Each record contains a frame object, filename, line number, function
        name, a list of lines of context, and index within the context."""
        framelist = []
        if etb is not None:
            while etb is not None:
                framelist.append((etb.tb_frame,
