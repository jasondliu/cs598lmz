import _struct
import binascii
import struct
import time

# this is the default value of the maximum packet size
# used by the pcap library to capture packets
#
# it is defined in the pcap/bpf.h header file
#
# as far as I know, it is not possible to change this
# value at runtime
#
# this value is used to set the sock_buff_size parameter
# of the socket.setsockopt function
#
# it is also used to set the bufsize parameter of the
# socket.recvfrom function
#
# I have chosen the following value because it is the
# minimum value that allows to capture jumbo frames
# (i.e. frames with a size greater than 1500 bytes)
#
# if you want to capture smaller frames, you can use
# the following values:
#
# 2048 for standard ethernet frames (i.e. frames with a
# size less or equal to 1500 bytes)
#
# 2304 to capture VLAN tagged frames (i.e. frames with a
# size less or equal to 1518 bytes)
#
# 2896 to
