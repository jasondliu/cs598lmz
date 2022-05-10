import socket
socket.if_indextoname('3')

import psutil
psutil.net_if_addrs()
for x in psutil.net_if_addrs()['Wi-Fi']:
    print(x[1])

# Change name of network interface
import os
os.system('netsh interface set interface name="Wi-Fi" newname="newname"')
os.system('netsh interface set interface name="newname" newname="Wi-Fi"')

# Check network interface name
import sys, paramiko
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.WarningPolicy)
client.connect(sys.argv[1], username='user', password='password')
stdin, stdout, stderr = client.exec_command('ifconfig')
print(stdout.readlines())

# Change network interface name using ssh
import sys, paramiko
client = paramiko.SSHClient()
client.load_system_host_keys()
