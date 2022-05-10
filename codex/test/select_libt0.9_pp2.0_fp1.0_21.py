import select
import socket
import sys
import traceback
from threading import Thread
from typing import List

import pyte

from Jumpscale import j
from .UASTypes.UASClientMessage import UASClientMessage
from .UASTypes.UASClientMessageWrapper import UASClientMessageWrapper

# from .UASProcess import UASProcess

logger = j.logger.get("j.tools._process.UASProcess")


class UASProcess(j.baseclasses.JSBaseClass):
    """
    Description of what this process does

    bcdb = j.data.bcdb.get("test")
    bcdb.reset()
    bcdb.reset()

    This needs to be the client app on the node

    """

    def __init__(self, cmd="", env={}, shell=True, debug=False):

        self._bcdb = j.data.bcdb.get("test")
        self._bcdb.reset()

        assert isinstance(cmd, str)
        self._cmd = cmd
        self._env = env
