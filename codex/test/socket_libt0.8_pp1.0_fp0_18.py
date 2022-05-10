import socket
import struct
import sys
import time

from optparse import OptionParser

ICMP_ECHO_REQUEST = 8
ICMP_CODE = socket.getprotobyname('icmp')
IP_CODE = socket.getprotobyname('ip')
MAX_HOPS = 30
TIMEOUT = 2.0
TRIES = 2

def checksum(source_string):
    sum = 0
    countTo = (len(source_string) / 2) * 2
    count = 0
    while count < countTo:
        thisVal = ord(source_string[count + 1])*256 + ord(source_string[count])
        sum = sum + thisVal
        sum = sum & 0xffffffff
        count = count + 2
    if countTo < len(source_string):
        sum = sum + ord(source_string[len(source_string) - 1])
        sum = sum & 0xffffffff
    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
