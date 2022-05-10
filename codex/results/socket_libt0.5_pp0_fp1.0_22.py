import socket, struct

def ip2long(ip):
    """
    Convert an IP string to long
    """
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]

def long2ip(longip):
    """
    Convert a long to IP string
    """
    return socket.inet_ntoa(struct.pack('!L', longip))

def ip2bin(ip):
    """
    Convert an IP string to binary string
    """
    return bin(ip2long(ip))[2:]

def bin2ip(bin):
    """
    Convert a binary string to IP string
    """
    return long2ip(int(bin, 2))

def ip2hex(ip):
    """
    Convert an IP string to hex string
    """
    return hex(ip2long(ip))[2:]

def hex2ip(hex):
    """
    Convert a hex string to IP string
    """
    return long2ip(int(hex, 16))

def ip2dec(
