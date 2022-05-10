import socket
# Test socket.if_indextoname(), bug #6785.
import subprocess
import threading
import time
import unittest

def if_nametoindex(ifname):
    popen = subprocess.Popen('/sbin/ifconfig',
                             shell=True, stdout=subprocess.PIPE)
    popen.stdout.readline()
    while True:
        line = popen.stdout.readline()
        ifline = line.split(b':')
        if len(ifline) > 1 and ifline[0] == ifname:
            break
    else:
        return 0
    # Work around an old bug in Linux's ifconfig: it might not print the
    # trailing newline.
    if line[-1:] != b'\n':
        line = line + b'\n'
    popen = subprocess.Popen('/bin/netstat', shell=True, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE)
    try:
        popen.stdin.write(line)
    except
