import select

import logging
logger = logging.getLogger('pyserial')

def serial_for_url(url, *args, **kwargs):
    """
    Create a serial instance for the given URL.
    If a scheme is given, it is used to look up a handler.
    If no scheme is given, the default scheme ``'serial'`` is used.
    """
    global _serial_classes
    scheme, _, path, _, _, _ = urlparse(url)
    if not scheme:
        scheme = 'serial'
    #print(scheme)
    if scheme in _serial_classes:
        cls = _serial_classes[scheme]
    else:
        raise ValueError("unknown URL scheme %r" % scheme)
    return cls(path, *args, **kwargs)

class Serial(io.RawIOBase):
    """
    Serial port implementation.

    A serial port object is created with the :meth:`~serial.Serial`
    class. It provides **all** functionality of the underlying port
    implementation (see below for a
