fn = lambda: None
gi = (i for i in ())
fn.__code__ = stackless.Schedule.__code__

# these test the effects of scheduler code on the reactor
def raising_wrapped_function(function_name):
    """
    Return wrapped function which raises exception.

    @type function_name: C{str}
    @param function_name: Name of function to wrap.

    @rtype: function
    @return: Wrapped function.
    """
    function = getattr(reactor, function_name)

    def wrapped_function(*args, **kwargs):
        """
        Raise an exception.
        """
        raise Exception("FOO")

    return wrapped_function

def clear_wrapped_function(function_name):
    """
    Return wrapped function which clears reactor attribute.

    @type function_name: C{str}
    @param function_name: Name of function to wrap.

    @rtype: function
    @return: Wrapped function.
    """
    function = getattr(reactor, function_name)

    def wrapped_function(*args, **kwargs):
        """
        Clear reactor attribute and call
