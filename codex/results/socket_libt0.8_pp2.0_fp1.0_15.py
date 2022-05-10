import socket
import sys
import getopt
import threading
import subprocess
import hashlib
import os
import base64
import time

# global vars for the server
listen = False
command = False
upload = False
execute = False
target = ""
upload_destination = ""
port = 0

#define the usage
def usage():
    print "BHP Net Tool"
    print
    print "Usage : bhpnet.py -t target_host -p port"
    print "-l --listen - listen on [host]:[port] for incoming connections"
    print "-e --execute=file_to_run - execute the given file upon receiving a connection"
    print "-c --command - initialize a command shell"
    print "-u --upload=destination - upon receiving connection upload a file and write to [destination]"
    print
    print 
    print "Examples :"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
    print "bhpnet.py -t 192.168.0.1 -p 5
