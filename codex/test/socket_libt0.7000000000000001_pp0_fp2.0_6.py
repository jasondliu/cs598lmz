import socket
import time
import sys
import os
from struct import pack, unpack

def read_hex(hex_file):
    hex_file = hex_file.split('\n')
    hex_start_addr = 0x00000000
    address = 0
    image = []
    for line in hex_file:
        if line[:1] == ':':
            line_data = unpack('>BHB' + str(len(line) - 11) + 's', line[1:])
            line_data = [line_data[0]] + list(unpack(str(line_data[0]) + 'B', line_data[3]))
            if line_data[1] != address:
                print('address does not match the expected address')
            if line_data[1] == 0:
                hex_start_addr = line_data[2] << 4
                address = hex_start_addr
            else:
                address = address + line_data[0]
            if line_data[0] == 0:
                break
