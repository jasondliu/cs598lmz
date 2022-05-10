import socket
# Test socket.if_indextoname()
#
# This test is a simple check of the socket.if_indextoname()
# method. The test is performed by getting the network
# interfaces on the test machine and checking that each
# interface name is returned by socket.if_indextoname()
#
# To check the test manually, you can use the following
# commands on a linux machine:
#
#   $ ifconfig -a
#   eth0      Link encap:Ethernet  HWaddr 00:0C:29:B1:F5:04
#             inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
#             inet6 addr: fe80::20c:29ff:feb1:f504/64 Scope:Link
#             UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
#             RX packets:320 errors:0 dropped:0 overruns:0 frame:0
#             TX packets:180 errors:0 dropped:0 overruns:0 carrier:0
#             collisions:
