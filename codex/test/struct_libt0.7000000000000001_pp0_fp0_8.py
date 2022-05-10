import _struct

from . import config, data, exceptions, files, messages, queries, utils

from .utils import debug


class Client(object):
    '''
    Client for the various methods and queries for interacting with the
    Transmission bittorrent client.

    Parameters
    ----------
    host : str
        The host of the server.
    port : int
        The port of the server.
    auth : tuple of str
        The username and password to authenticate with.
    '''

    def __init__(self, host='localhost', port=9091, auth=None):
        self.config = config.Config(self)
        self.files = files.Files(self)
        self.debug = False
        self.session_id = None

        self.url = 'http://{0}:{1}'.format(host, port)
        self.auth = auth

    def _call(self, method, arguments=None, need_session_id=True,
              return_data=True):
        if arguments is None:
            arguments = {}

