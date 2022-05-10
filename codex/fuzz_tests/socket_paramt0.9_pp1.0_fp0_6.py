import socket
socket.if_indextoname(1)

| = socket.socket(socket.AF_PACKET,socket.SOCK_RAW)
#socket.AF_PACKET type of address to receive from : MAC-Address
#socket.SOCK_RAW Set socket to raw mode so it can send multi bytes data, as Ethernet Frames

# 1) Insert Sniffer details in Ethernet Frame
# ------------------------ Ethernet Frame ----------------------------
#    Destination MAC-Address                                           
#    Source MAC-Address                                             
#    Type : 0X008 (IP)                                                                
# --------------------------------------------------------------------
#
# 2) Insert IP packet details in IP packet                                                                                                                                                    
# ------------------- IP Packet --------------------------------------
#  Version (4 Bits)   Internet Header Length (IHL) (4 Bits)
#     0X4                  0X5                 
#   Service Type (8 Bits)
#  Total Length (16 Bits)
#            28 Bytes    
# Identification (16 Bits)
#      0 
#  Flags (3 Bits)        Fragment Offset (13 Bits)
#    0                        0
#  Time To
