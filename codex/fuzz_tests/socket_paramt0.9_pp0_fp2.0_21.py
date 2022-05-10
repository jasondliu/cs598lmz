import socket
socket.if_indextoname(2)

(1, 2, '', '')
(1, 2, 'love', '')

(1, 0, '', '')
(1, 0, '', '')
[Finished in 0.5s]
(1, 2, 'love', '')
(1, 2, '', '')

(1, 0, '', '')
(1, 0, '', '')
(1, 2, 'love', '')
(1, 2, '', '')

(1, 2, 'love', '')
(1, 2, '', '')
[Finished in 0.6s]
'''

pre = 0
pre_index = 0
#to find the change when packets is sended.

while True:
    while(1):

        cur = 0
        cur_index = 0
        s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

        pkt = s.recvfrom(65535)
        pkt = pkt[
