import socket
socket.if_indextoname('4')

#반대로 주소를 인덱스로 바꾸기
socket.if_indextoname(2)

#네트워크 인터페이스 이름을 인덱스로 바꾸기
socket.if_nametoindex('eth0')
