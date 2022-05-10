import socket
socket.if_indextoname(8)

#%%
#Interface Names
#Find interface names of all interface
import psutil

net_if_addrs = psutil.net_if_addrs()
for k,v in net_if_addrs.items():
    print(k)

#%%
print(psutil.net_if_addrs())

#%%
#IP Addresses
#Print IP addresses of all interface
import psutil
print(psutil.net_if_addrs())

#%%
#MAC Addresses
#Print MAC address of all interface
import psutil
nets = psutil.net_if_addrs()
for i,j in nets.items():
    print(i,":",j[0].address)

#%%
#Gateway Addresses
#Print gateway addresses of all interface
import psutil
nets = psutil.net_if_addrs()
for i,j in nets.items():
    print(i,":",j[0].address)

#%%
#Netmask
#Print Netmask for all interfaces
import psutil
