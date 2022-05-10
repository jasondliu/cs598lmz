import mmap
import os
import re
import subprocess
import sys
import time

from . import utils

def get_pid_from_name(name):
    pid_list = []
    pid_list = [pid for pid in os.listdir('/proc') if pid.isdigit()]
    for pid in pid_list:
        try:
            with open(os.path.join('/proc', pid, 'cmdline'), 'rb') as f:
                if name in f.read():
                    return pid
        except IOError: # proc has already terminated
            continue
    return None

def get_pid_from_port(port):
    """
    Return the pid of the process that is listening on the given port.
    """
    cmd = 'netstat -lntp | grep LISTEN | grep %s' % port
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = proc.communicate()
    if err:
        raise Exception('Failed to get pid from port: %s'
