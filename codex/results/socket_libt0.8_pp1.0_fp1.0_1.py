import socket
import sys
import struct
import time

# https://www.netresec.com/?page=Blog&month=2016-10&post=Mac-OS-X-Random-MAC-Address-Generation
# Mac OS X Random MAC Address Generation
def gen_mac_address():
    mac_address = '02:00:00:00:00:%02x' % random.randint(0, 255)
    mac_value = int(mac_address.split(':')[5], 16) & 0xfe
    mac_address = mac_address.split(':')[0:5] + [hex(mac_value)[2:]] + [mac_address.split(':')[6]]
    mac_address = ':'.join(mac_address)
    return mac_address

# https://stackoverflow.com/questions/29306747/python-send-raw-ethernet-frame
# Python send raw ethernet frame
def send_arp_packet(dest_addr, source_addr, source_mac, is_reply, dest_mac=None, dest
