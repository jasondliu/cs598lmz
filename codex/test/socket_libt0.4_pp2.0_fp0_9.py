import socket
import struct
import sys
import time
import traceback

# pylint: disable=import-error
import paramiko

import lib.libsf as libsf
from lib.libsf import mylog
import lib.sfdefaults as sfdefaults
from lib.action_base import ActionBase
from lib.datastore import SharedValues

class SshCommandAction(ActionBase):
    class Events:
        """
        Events that this action defines
        """
        FAILURE = "FAILURE"

    def __init__(self):
        super(self.__class__, self).__init__(self.__class__.Events)

    def ValidateArgs(self, args):
        libsf.ValidateArgs({"host" : libsf.IsValidIpv4Address,
                            "username" : None,
                            "password" : None,
                            "command" : None,
                            "timeout" : libsf.IsInteger,
                            "debug" : None},
            args)

