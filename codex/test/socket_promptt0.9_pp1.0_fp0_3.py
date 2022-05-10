import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(2))
print(socket.if_indextoname(1))
print(socket.if_indextoname(0))
ISQA39_DataExercise8 = True
print(ISQA39_DataExercise8)
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:02:38 2020

@author: td01
"""
import socket
# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))
print(socket.if_nametoindex('eth1'))
print(socket.if_nametoindex('eth0'))
ISQA39_DataExercise9 = True
print(ISQA39_DataExercise9)
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:06:20 2020

@author: td01
"""
import socket
# Test socket.linger()
s = socket.socket()
