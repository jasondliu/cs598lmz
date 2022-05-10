import socket
socket.if_indextoname('7', 'fe80::ba27:ebff:fe04:81df', '24')

#Server:
socket.ip_address_list()

#Socket Flags
"""
Cafes:
    SOCK_STREAM: TCP (connection oriented).
    SOCK_DGRAM: UDP (connectionless).
    SOCK_RAW: direct access to the underlying transport protocol (ICMP).
    SOCK_SEQPACKET: data packets are sequenced.
    SOCK_PACKET: raw ethernet frame.
Taverns:
    SO_DEBUG: socket-level debugging info.
    SO_REUSEADDR: allow reuse of local address.
    SO_KEEPALIVE: send periodic checks to detect broken connections.
    SO_DONTROUTE: bypass routing.
    SO_LINGER: linger on close if data is present (figure 6-5).
    SO_BROADCAST: can send to broadcast address.
    SO_OOBINLINE: out-of-band data is placed inline.
    SO_SNDBUF: send buffer size,
    SO_
