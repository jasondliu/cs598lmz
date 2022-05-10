import ctypes
import ctypes.util
import threading
import sqlite3

from pymongo import MongoClient

from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet, ethernet, arp, ipv4, udp, tcp, icmp
from ryu.lib.packet import ether_types

class MacLearning(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
    _CONTEXTS = { 'dpset': dpset.DPSet }
    def __init__(self, *args, **kwargs):
        super(MacLearning, self).__init__(*args, **kwargs)
        self.mac_to_port = {}
        self.dpset = kwargs['dpset']
        self.datapaths
