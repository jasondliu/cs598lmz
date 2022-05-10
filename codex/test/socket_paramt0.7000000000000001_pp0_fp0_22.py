import socket
socket.if_indextoname('5')

#%%
import network
import esp32

nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.scan()
nic.config(dhcp_hostname='myesp32')
nic.connect('<your_essid>', '<your_password>')
nic.ifconfig()

#%%
import gc
gc.collect()
gc.mem_free()

#%%
import webrepl
webrepl.start()

#%%
import webrepl_setup
webrepl.start()

#%%
import upip
upip.install('micropython-uasyncio.core')

#%%
import uasyncio as asyncio
import utime

async def print_time():
    while True:
        print(utime.localtime())
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(print_time())
loop.close()

#%%
import sys
sys.implementation

