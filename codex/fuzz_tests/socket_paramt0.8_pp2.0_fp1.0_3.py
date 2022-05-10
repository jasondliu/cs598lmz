import socket
socket.if_indextoname(3)

'''

对网卡设置IP地址
===================
sudo ifconfig [网卡名] [IP地址] netmask [子网掩码]

ifconfig lo0 netmask 255.255.255.0 up
route add default gw 192.168.0.1 lo0

'''
