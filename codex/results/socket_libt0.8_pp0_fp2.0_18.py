import socket
import superdecimal
import threading

#first stage
def run1():
    #ask for an ip address and port to connect to
    print "syntax: <ip>:<port>\n"
    print "Connecting to a host"
    ip = ''
    port = ''
    start = False
    while(not start):
        print "Enter server address:"
        addr = raw_input()
        if(addr.rfind(':') == -1):
            print "Syntax error. Please try again\n"
            continue
        ip = addr[0:addr.rfind(':')]
        port = addr[addr.rfind(':')+1:]
        if(len(ip) > 0 and len(port) > 0):
            start = True
        else:
            print "Syntax error. Please try again\n"
            continue

    print "Connecting to server..."
    #connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.connect(('localhost',int(
