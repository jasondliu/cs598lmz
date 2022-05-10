import socket
socket.if_indextoname("3")

#%%
import subprocess
import os
import sys
import re

def get_ip_address():
    if os.name == 'nt':
        command = "ipconfig"
    else:
        command = "ifconfig"
    output = subprocess.check_output(command)
    return re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', output)

#%%
print(get_ip_address())

#%%
print(get_ip_address()[0])

#%%
print(get_ip_address()[1])


#%%
import socket
print(socket.gethostname())

#%%
import socket
print(socket.gethostbyname(socket.gethostname()))

#%%
import socket
print(socket.gethostbyname(socket.gethostname()))

#%%
import socket

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.
