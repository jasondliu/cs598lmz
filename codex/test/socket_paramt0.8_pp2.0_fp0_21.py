import socket
socket.if_indextoname(6)#6是wlan0
import commands
import re

class NetDetect(object):
    """docstring for NetDetect"""
    def __init__(self):
        super(NetDetect, self).__init__()
        self.gate_count = 1
        self.gate_ip = []
        self.gate_mac = []

    def getIface(self):
        self.gate_count = 0
        self.iface = []
        self.iface_list = commands.getoutput("ifconfig | cut -d ' ' -f1|sed 's/://g'").split("\n")
        for i in self.iface_list:
            if re.match("^eth\d$",i) or re.match("^wlan[0-9]$",i):
                self.iface.append(i)
                self.gate_count = self.gate_count + 1
        return self.iface

    def getGate(self):
        self.gate_ip = []
        self.gate_mac = []
