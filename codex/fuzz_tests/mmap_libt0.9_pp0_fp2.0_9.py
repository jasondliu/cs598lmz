import mmap
import sys
import time
import yaml
import re
import os

print_port = True
list_ports = False

def get_running_vmid():
    #pid_file = subprocess.check_output(['pgrep', '-f', '^oai test_ue.py'])
    pid_file = subprocess.check_output(['pgrep', '-f', '\.bin.*test_ue\.py'])
    return pid_file.decode('utf-8').strip()

def test_dynamic_vlc_port(vlc_port):
    """
       Test if vlc_port is already in use, assuming we are connected to the machine
       where the test_ue.py program is running (Targets.ARM).
       Called in do_generate, test_vlc_port_free when list_ports is set.
    """
    global list_ports
    if not list_ports:
        if type(vlc_port) is not int:
            vlc_port = int(vlc_port)
        sock = socket.
