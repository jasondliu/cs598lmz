import socket
socket.if_indextoname(1)

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("office_wifi", "wifi_password")
while not wifi.isconnected():
    pass

print(wifi.ifconfig())
