import socket
socket.if_indextoname(if_index)

#%%
# get if_index
import socket
socket.if_nametoindex('eth0')

#%%
# get all interface names
import netifaces
netifaces.interfaces()

#%%
# get all interface addresses
import netifaces
netifaces.ifaddresses('eth0')

#%%
# get all interface IP addresses
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET]

#%%
# get all interface MAC addresses
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK]

#%%
# get all interface IP addresses
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

#%%
# get all interface MAC addresses
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

#%%
# get all interface IP addresses
import net
