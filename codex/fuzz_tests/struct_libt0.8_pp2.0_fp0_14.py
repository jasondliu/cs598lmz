import _struct

class ProxyProtocolHeader(object):
    """ProxyProtocolHeader
    Proxy Protocol Header
    """

    def __init__(self, type_=None, src_addr=None, dst_addr=None, src_port=None, dst_port=None):
        self._type = None
        self._src_addr = None
        self._dst_addr = None
        self._src_port = None
        self._dst_port = None
        self.__id_ref = None

        if type_ is not None:
            self.type = type_
        if src_addr is not None:
            self.src_addr = src_addr
        if dst_addr is not None:
            self.dst_addr = dst_addr
        if src_port is not None:
            self.src_port = src_port
        if dst_port is not None:
            self.dst_port = dst_port

    @property
    def type(self):
        """ Get type value.

            Notes:
                Proxy Protocol Header Type: TCP4, TCP6
