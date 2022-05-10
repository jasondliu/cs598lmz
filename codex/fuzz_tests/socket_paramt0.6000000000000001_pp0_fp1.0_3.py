import socket
socket.if_indextoname(12)

# import subprocess
# subprocess.check_call(['ifconfig', 'eth0', 'up'])
# subprocess.check_call(['ifconfig', 'eth0', 'hw', 'ether', '00:00:00:00:00:01'])

import time
time.sleep(1)
print "Started"

# import os
# os.system("ifconfig eth0 up")
# os.system("ifconfig eth0 hw ether 00:00:00:00:00:01")
# os.system("ifconfig eth0 192.168.1.1")

# from subprocess import Popen, PIPE
# Popen(['ifconfig', 'eth0', 'up'], stdout=PIPE)
# Popen(['ifconfig', 'eth0', 'hw', 'ether', '00:00:00:00:00:01'], stdout=PIPE)
# Popen(['ifconfig', 'eth0', '192.168.1.1'], stdout=PIPE)

import commands

