import socket
socket.if_indextoname(3)

import json
import requests
import os
import subprocess
import time

def get_ip(iface):
    command = "ip addr show %s" % iface
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return output.decode('utf-8').split('inet ')[1].split('/')[0]

def get_mac(iface):
    command = "ip addr show %s" % iface
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return output.decode('utf-8').split('link/ether ')[1].split(' ')[0]

def get_dns_servers(iface):
    command = "cat /etc/resolv.conf"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
