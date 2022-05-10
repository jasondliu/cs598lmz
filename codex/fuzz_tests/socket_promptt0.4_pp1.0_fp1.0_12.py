import socket
# Test socket.if_indextoname()

import os, sys
import unittest
import test.test_support

INTERFACES = {
    0: 'lo',
    1: 'eth0',
    2: 'eth1',
    3: 'sit0',
    4: 'wlan0',
    5: 'wlan1',
    6: 'vmnet1',
    7: 'vmnet8',
    8: 'ppp0',
    9: 'ppp1',
    10: 'ppp2',
    11: 'tun0',
    12: 'tun1',
    13: 'tun2',
    14: 'tun3',
    15: 'tun4',
    16: 'tun5',
    17: 'tun6',
    18: 'tun7',
    19: 'tun8',
    20: 'tun9',
    21: 'tun10',
    22: 'tun11',
    23: 'tun12',
    24: 'tun13',
    25: 'tun14',
    26: 'tun15',
    27: 'tun
