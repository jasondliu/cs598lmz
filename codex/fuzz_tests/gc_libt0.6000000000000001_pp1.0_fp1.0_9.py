import gc, weakref

from LLRPTestCase import LLRPTestCase
from llrp_proto import *

class test_ReaderConfiguration(LLRPTestCase):

    def setUp(self):
        self.cmd = {
            'Name':'ReaderConfiguration',
            'MessageID':242,
            'ResetToFactoryDefault':1
        }
        self.cmd_rsp = {
            'Name':'READER_EVENT_NOTIFICATION',
            'MessageID':242,
            'LLRPStatus':{'StatusCode':0},
            'ReaderEventNotificationData':{
                'UTCTimestamp':{'Microseconds':88888888},
                'ConnectionAttemptEvent':{
                    'ConnectionStatus':0,
                    'ReaderHostName':'localhost'
                }
            }
        }
        self.cmd_spec = {
            'Name':'ReaderConfiguration',
            'MessageID':242,
            'ResetToFactoryDefault':1
        }
        self.cmd_rsp_spec = {
            'Name':'READER_EV
