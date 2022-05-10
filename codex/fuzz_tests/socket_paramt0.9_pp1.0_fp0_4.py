import socket
socket.if_indextoname('12')

# -*- coding: utf-8 -*-
import socket
CMD_TURN         = 0x1
CMD_TILT         = 0x2
CMD_PAN          = 0x3
CMD_TOPTILT      = 0x4
CMD_LOGIN        = 0x5
CMD_UPGRADE_APP  = 0x6
CMD_SHUTDOWN     = 0x7
CMD_HARTBEAT_    = 0x8
CMD_SERVER_INFO  = 0x9
CMD_GIMBAL_INFO  = 0x10
CMD_LICENSE      = 0x11
CMD_HARTBEAT_IP  = 0x12
CMD_GIMBAL_STATE = 0x13
CMD_RESET        = 0x14
CMD_WIFI         = 0x15
CMD_CUSTOM       = 0x16
FLAG_SHUTDOWN        = 0x1
FLAG_RESTART         = 0x2
FLAG_UPGRADE_APP    
