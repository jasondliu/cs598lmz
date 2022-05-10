import socket
socket.if_indextoname("12")

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",4242))#doesn't allow access to port 4242, even for connected devices
s.listen(5)
while True:
    (clientsocket, address)=s.accept()
    rd=clientsocket.recv(5000).decode()
    items=rd.split("\r\n")
    url=items[0].split(" ")[1]
    http_pos=url.find("://")
    if(http_pos==-1):
        temp=url
    else:
        temp=url[(http_pos+3):]
    port_pos = temp.find(":")
    webserver_pos = temp.find("/")
    if webserver_pos == -1:
        webserver_pos=len(temp)
    webserver = ""
    port = -1
    if(port_pos==-1 or webserver_pos<port_pos):
        port=
