import socket
socket.if_indextoname(9)

import os
os.listdir('/etc')
os.listdir(b'/etc')
os.scandir('/etc')

import subprocess
subprocess.call(['ls', '-l'], stdout=subprocess.DEVNULL)
subprocess.call(['ls', '-l'], stdout=subprocess.PIPE)

import subprocess
subprocess.call(['ls', '-l'], stdout=subprocess.DEVNULL)
# try:
#     subprocess.call(['ls', '-l'], stdout=subprocess.PIPE)
# except ValueError as e:
#     print(e)

import subprocess
subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

import os
os.system('ls -l')

import os
