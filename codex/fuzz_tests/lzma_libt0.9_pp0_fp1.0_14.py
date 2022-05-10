import lzma
lzma.LZMAError

from .xz_marshal import XZPickler, XZUnpickler

class XZPickler(pickle.Pickler):
    """Subclass to pickle via xz compression.

    Example:

    xzpickler = XZPickler(open("myfile", "w"))
    xzpickler.dump(myobject)

    """

    def __init__(self, file, protocol=None):
        """Compress data with xz, directly to file

        :param file: A file object open with mode 'wb'
        :param protocol: A pickle protocol
        """
        self.xz_file = lzma.LZMAFile(file, "w")
        # use the cStringIO for pickling, to be written to lzma
        self.file = cStringIO.StringIO()
        # pickle.Pickler has no 'protocol' argument
        pickle.Pickler.__init__(self, self.file)

    def dump(self, obj):
        """Dump obj in compressed format
