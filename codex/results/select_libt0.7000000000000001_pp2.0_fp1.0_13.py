import selectors
import sys
import time

from functools import partial

from scapy.layers.inet import UDP
from scapy.utils import PcapReader

from config import *
from log import log
from model import *
from pcap_reader import *
from udp_client import *
from udp_server import *
from util import *
from tun import *
from nat import *


def main():

    # 初始化日志
    log.init_log(LOG_DIR)

    # 初始化锁
    lock = threading.Lock()

    # 初始化配置
    config.init(CONF_PATH)

    # 初始化
    tun.init(TUN_DEV, TUN_ADDR, TUN_MASK)

    # 初始化nat
    nat.init(NAT_TABLE_PATH)

    # 初始化udp server
    udp_server.init(UDP_SERVER
