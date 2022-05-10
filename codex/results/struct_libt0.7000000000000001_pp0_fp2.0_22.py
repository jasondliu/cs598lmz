import _struct

from dpkt import pcap, pcapng
from dpkt.compat import compat_struct
from dpkt.utils import inet_ntoa

__all__ = ['Reader']


class Reader(object):
    """
    Read packet capture files.

    Attributes:
        fd: file descriptor for reader of capture file
        fd.tell(): offset of capture file pointer
        fd.seek(): position capture file pointer
        fd.read(): read data from capture file

    Example:
        >>> import pcap
        >>> c = pcap.Reader(open('test.pcap'))
        >>> for ts, buf in c:
        ...     pass
    """

    def __init__(self, fd):
        """Initialize object with file descriptor `fd`."""
        self.fd = fd
        self.fd.seek(0)
        try:
            self.__fh = self.fd.fileno()
        except (AttributeError, io.UnsupportedOperation):
            self.__fh = None
        self.__reader = self.
