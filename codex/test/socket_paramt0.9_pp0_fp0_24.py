import socket
socket.if_indextoname(5)
#'enp0s25'
                    
import netifaces
netifaces.ifaddresses('enp0s25')[netifaces.AF_LINK][0]['addr']
#'70:4d:7b:12:d4:70'

import netifaces
netifaces.ifaddresses('lo')[netifaces.AF_INET][0]['addr']
#'127.0.0.1'

import psutil, datetime
boot = psutil.boot_time()
dt = datetime.datetime.fromtimestamp(boot)
print(dt)

import netifaces
netifaces.ifaddresses('enp0s25')[netifaces.AF_INET][0]['addr']

import socket
socket.if_indextoname(5)

import socket
socket.gethostbyname(socket.gethostname())

Response: ('127.0.0.1', ['loopback', 'localhost.localdomain', 'localhost'], ['::1'])
