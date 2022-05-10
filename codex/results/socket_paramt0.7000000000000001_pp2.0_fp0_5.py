import socket
socket.if_indextoname(12)

# 공유기에서 정의한 인터페이스 이름
# 공유기에서 해당 이름으로 된 인터페이스를 만듬
# 12번 인터페이스에 바인드하는 것이 아님
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
s.bind(("eth0", socket.htons(0x0800)))
# 네트워크 인터페이스가 사라지는 이
