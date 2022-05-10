import socket
import time
import sys

def usage():
    print("Usage: {0} <host> <port> <file>".format(sys.argv[0]))
    print("Example: {0} 127.0.0.1 21 ftp.txt".format(sys.argv[0]))

def valid_ipv4(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:
        return False
    return True

def valid_port(port):
    try:
        port = int(port)
    except:
        return False
    if port < 1 or port > 65535:
        return False
    return True

def valid_ipv4_port(address_port):
    address, port = address_port.split(':')
    if not valid_ipv4(address):
        return
