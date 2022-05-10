import weakref


def pthread(fcn):
    """ Decorator that runs a method in a separate daemonic thread. """
    @wraps(fcn)
    def _threaded(*args, **kwargs):
        inst = args[0]
        th = Thread(target=fcn, args=(inst,) + args[1:], kwargs=kwargs)
        th.daemon = True
        th.start()
    return _threaded


def sin(x, p=None):
    """ Returns the sin of x. If p is specified, the sin of x is raised to
    the pth power.
    """
    y = numpy.sin(numpy.array(x, dtype=float))
    return (y ** p) if p is not None else y


def cos(x, p=None):
    """ Returns the cos of x. If p is specified, the cos of x is raised to
    the pth power.
    """
    y = numpy.cos(numpy.array(x, dtype=float))
