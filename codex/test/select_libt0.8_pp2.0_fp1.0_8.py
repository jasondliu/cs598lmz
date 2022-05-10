import select
#import socket
import struct
import sys
import threading
import time

#class NetworkDevice(object):
#    def __init__(self, name):
#        self.arp = {}
#        self.mac = json.loads(subprocess.check_output(['ip', 'link', 'show', name]).decode()).get('link/ether')
#        self.fd = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ARP))
#        self.fd.bind((name, ETH_P_ARP))
#
#    def start(self):
#        def _receive():
#            while True:
#                raw_data, ancdata, msg_flags, addr = self.fd.recvmsg(1500)
#                arp = Arp(raw_data)
#                self.arp[arp.sender_ip_address] = arp.sender_mac_address
#
#        thread = threading.Thread(target=_receive)
#        thread.daemon =
