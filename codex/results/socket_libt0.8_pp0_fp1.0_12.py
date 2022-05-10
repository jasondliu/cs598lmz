import socket
from threading import Thread
from time import sleep
import random


from test_util import *
from test_header import *
from pkt import *

from iproute2_client import *
from port_mapping import *
from common.types import FlowType, BlockType
from common.switch import Switch
from common.router import Router

from parse_config import parse_config

class Topology:
    def __init__(self, config_filename):
        self.config = parse_config(config_filename)
        self.switches = dict()
        self.routers = dict()
        self.local_ip = get_local_ip()
        self.init_topology()

    ################################################################################
    #                   set up the test topology
    ################################################################################
    def init_topology(self):
        switch_num = self.config['switch_num']
        for i in xrange(switch_num):
            self.switches[i] = Switch(self.config['switches'][i])

        router_num = self.
