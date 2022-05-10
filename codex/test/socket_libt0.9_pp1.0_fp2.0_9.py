import socket
import time, re

#Create a UDP socket
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

clientsocket.sendto('wl phy_rssi', ('192.168.1.1', 1234))
clientsocket.settimeout(0)

cpt = 0
t = time.time()

