import select
import pygame
import time
from contextlib import closing

from config import *
from lirc import *

class LircDevice(object):
    def __init__(self, device):
        self.configfile = "lircd.conf"
        self.context = lirc_init(self.configfile, blocking=False)

        self.socket = lirc_nextcode()

        self.device= "/dev/lircd"
        self.poller = select.poll()
        self.poller.register(self.socket[0], select.POLLIN)

    def __del__(self):
        lirc_deinit()

    def get_next_ir(self):
        status = self.poller.poll(0)
        if not status:
            return False
        else:
            code = lirc_nextcode()
            # print(code)
            data = [x for x in code if ( x[:len(IR_HEADER_ID)] == IR_HEADER_ID)]
            # print(data)
            self.codes = [x
