import socket
# Test socket.if_indextoname() (LP: #1469226)
if_indextoname = socket.if_indextoname
try:
    if_indextoname(1)
except ValueError:
    print("SKIP")
    raise SystemExit

import network

sta_if = network.WLAN(network.STA_IF)
sta_if.config(dhcp_hostname="test_dhcp_hostname")
sta_if.active(True)
sta_if.connect("essid", "password")

import time
while not sta_if.isconnected():
    print(".", end="")
    time.sleep(1)
print()

# Wait for DHCP lease
while not sta_if.ifconfig()[0]:
    time.sleep(1)

# Check assigned IP
print(sta_if.ifconfig())
