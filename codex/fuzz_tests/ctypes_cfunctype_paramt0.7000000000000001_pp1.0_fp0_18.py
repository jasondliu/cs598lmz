import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

# we need to store these somewhere that will survive
# being cleared by %reset -f in IPython
_callback_map = weakref.WeakValueDictionary()


def _callback(event, name):
    """The callback which gets installed into the ROOT TApplication"""
    assert event
    assert name

    # TODO: use pyROOT to convert event into a proper Python object
    try:
        _callback_map[name](event)
    except KeyError:
        # the callback has been removed
        pass


def connect(obj, signal, callback):
    """Connect a user callback to a ROOT signal

    Parameters
    ----------
    obj : ROOT object
        The object which will emit the signal
    signal : str
        The name of the signal to connect to on the object
    callback : callable
        The callback to execute when the signal is fired

    Returns
    -------
    disconnect : callable
        A function which disconnects the callback from the signal

    Examples
    --------
    >>> from rootpy.ROOT import TFile
    >>>
    >>> file = T
