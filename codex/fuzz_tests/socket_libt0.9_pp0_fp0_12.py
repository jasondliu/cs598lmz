import socket

def listenCom(req):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', 20001))
    s.settimeout(1)
    for i in range(3):
        try:
            b, addr = s.recvfrom(4096)
            s.sendto(req.encode(), addr)
        except (OSError, socket.timeout):
            try:
                b, addr = s.recvfrom(4096)
                s.sendto(req.encode(), addr)
            except (OSError, socket.timeout):
                try:
                    b, addr = s.recvfrom(4096)
                    s.sendto(req.encode(), addr)
                except (OSError, socket.timeout):
                    s.close()
                    print("Echo service timed out after 3 attempts")
                    return False
        if not b.decode() == req:
            s.close()
            print("Echo service returned something other than what it received")
            return False
   
