import weakref

from cplcom.server import CplComServer
from cplcom.client import CplComClient

from . import __version__


class CplComError(Exception):
    pass


class CplCom(object):
    def __init__(self, server_address=None, client_address=None):

        if server_address is None and client_address is None:
            raise ValueError("Either server_address or client_address must be set")

        if not hasattr(self, '_cpl_version'):
            self._cpl_version = __version__

        self._cpl_connection = None

        if server_address is not None:
            self._cpl_connection = weakref.ref(
                CplComServer(
                    server_address,
                    self,
                )
            )
        else:
            self._cpl_connection = weakref.ref(
                CplComClient(
                    client_address,
                    self,
                )
            )

    def process(self):
        self._cpl_connection().process()


