import _struct

class Aio(object):
    """
    Aio class
    """
    def __init__(self, dev, aio_ch):
        """
        Initialization method.
        
        @param dev: Device ID
        @param aio_ch: Aio channel
        """
        self.dev = dev
        self.aio_ch = aio_ch
        self.handle = ct.c_ulong()
        self.open()

    def __del__(self):
        """
        Destructor -- Closes the device.
        """
        if self.handle.value:
            self.close()

    def open(self):
        """
        Opens the device.
        """
        r = _udevice.UH_AioOpen(self.dev, self.aio_ch, ct.byref(self.handle))
        if r != _uerr.U_SUCCESS:
            raise IOError('UH_AioOpen failed with error code %d' % r)

    def close(self):
        """

