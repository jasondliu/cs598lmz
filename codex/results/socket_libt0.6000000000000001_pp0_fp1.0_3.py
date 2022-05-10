import socket
import subprocess
import time
import sys
import os
import json

class IP():
    def __init__(self, ip, subnet):
        self.ip = ip
        self.subnet = subnet
        self.octets = self.ip.split(".")
        self.net_id = self.octets[0] + "." + self.octets[1] + "." + self.octets[2] + "."
        self.broadcast = self.net_id + "255"
        self.hosts = int(self.subnet.split("/")[1]) - 2
        self.hosts_list = []
        self.scan_ip = []
        self.max_host = int(self.net_id.split(".")[3]) + self.hosts
        self.min_host = int(self.net_id.split(".")[3]) + 1
        self.data = []
        self.valid = False
        self.ping_data = []

    def host_generator(self):
        for i in range(self
