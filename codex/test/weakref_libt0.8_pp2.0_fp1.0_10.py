import weakref
import socket
import logging

from .. import rwm_client
from .. import rwm_common
from .. import json
from .. import events
from . import _rwmsg_agent as ra

class RWMsgAgent:
    '''
    RW.Msg agent
    '''
    def __init__(self, sockpath):
        self.sockpath = sockpath
        self.rwmain = None
        #logging.basicConfig(level=logging.DEBUG)
        self.rwlogger = logging.getLogger('RWMC.agent')
        self.rwlogger.setLevel(logging.DEBUG)
        self.log = self.rwlogger.debug
        self.rwmain = rwm_client.RWMsgMain(self)
        self.rwclient = rwm_client.RWMsg(self.rwmain)
        self.rwmain.start()

    def run(self):
        self.rwmain.loop()

    def shutdown(self):
        if self.rwclient:
            self.rwclient.disconnect()
