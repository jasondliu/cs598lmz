import socket
# Test socket.if_indextoname()
#
# $ nft add rule ip filter INPUT iifname "lo" accept

from dpkt import ip
from dpkt import tcp
from dpkt import udp

import ifaddr

from packetracer import packetracer

from packetracer.packetracer_meta import FIELD_FLAG_AUTOUPDATE


def test_basic():
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    s.bind((socket.if_indextoname(2), 3))
    s.close()


def test_packetracer_basic():
    iface = ifaddr.get_adapters()[0]
    s = packetracer.Socket()

    s.bind(iface.nice_name, type=packetracer.ETH_P_ALL)

    s.close()


def test_packetracer_tx_simple():
    iface = ifaddr.get_adapters()[0]

    eth = packetracer.Ethernet()
    eth.src = if
