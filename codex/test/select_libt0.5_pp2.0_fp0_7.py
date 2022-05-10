import select
import socket
import struct
import sys
import time

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-p", "--port", dest="port", type="int",
                  help="Port to listen on")
parser.add_option("-t", "--timeout", dest="timeout", type="int",
                  help="Timeout in seconds")
(options, args) = parser.parse_args()

def main():
    if not options.port:
        parser.error("You must specify a port")
    if not options.timeout:
        parser.error("You must specify a timeout")

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', options.port))
    s.setblocking(0)

    start_time = time.time()
    while True:
        result = select.select([s], [], [], 1)
        if result[0]:
            data, addr = s.recvfrom(1024)
