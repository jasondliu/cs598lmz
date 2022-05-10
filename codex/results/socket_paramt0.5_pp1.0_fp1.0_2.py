import socket
socket.if_indextoname(0x0a)

#%%
import netifaces
netifaces.interfaces()

#%%
netifaces.ifaddresses('wlp2s0')

#%%
netifaces.ifaddresses('wlp2s0')[netifaces.AF_INET][0]['addr']

#%%
import time
time.time()

#%%
import time
time.ctime()

#%%
import time
time.ctime(time.time())

#%%
import time
time.ctime(time.time()+86400)

#%%
import time
time.ctime(time.time()+86400*30)

#%%
import time
time.ctime(time.time()+86400*365)

#%%
import time
time.ctime(time.time()+86400*365*10)

#%%
import time
time.ctime(time.time()+86400*365*100)

#%%
import time
time.ctime(time.time()+86400*
