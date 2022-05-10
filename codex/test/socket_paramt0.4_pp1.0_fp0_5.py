import socket
socket.if_indextoname(1)

# 인터페이스 인덱스를 이름으로 변환
socket.if_nameindex()

# 인터페이스 이름을 인덱스로 변환
socket.if_nametoindex('lo')

# 인터페이스 정보를 얻음
socket.if_nameinfo(('127.0.0.1', 80))

# 호스트 이름을 IP 주소로 변환
socket.gethostbyname('localhost')

# IP 주소를 호스트 이름으로 변환
socket.gethostby
