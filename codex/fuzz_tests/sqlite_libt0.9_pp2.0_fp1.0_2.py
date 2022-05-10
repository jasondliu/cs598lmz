import ctypes
import ctypes.util
import threading
import sqlite3
import os
import httplib
import base64
import simplejson as json
import re
import socket
import array
import async_dispatcher


class RemoteController():
    """ Remote controller class """

    def __del__(self):
        """ Deletes the RemoteController object """
        self.quit()

    def __init__(self, dmobilec_path, http_port,
                 poll_interval, callback_callable):
        """ Initializes a RemoteController object

        :type dmobilec_path: str
        :type http_port: int
        :type poll_interval: int
        :type callback_callable: callable
        """

        log.debug('RemoteController.__init__()', self)

        # path of dmobilec binary
        self._dmessagemonitor_path = ''
        # constant for timeout for monitor - time for start/stop/...
        self._dm_timeout = 5

        # dmobilec path
        self._dmobilec_path = dmobilec_path
        self._http_port = http_port

        self
