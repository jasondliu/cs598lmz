import socket
socket.if_indextoname(2)

#ifconfig
import netifaces
print netifaces.interfaces()
print netifaces.ifaddresses('lo')
print netifaces.ifaddresses('eth0')

#netstat
import psutil
print psutil.net_io_counters(pernic=True)

#proc_stats
import win32process, win32api
print win32process.GetProcessMemoryInfo(win32api.GetCurrentProcess())

#ip
import commands
print commands.getoutput('ipconfig')
