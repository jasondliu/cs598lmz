import socket
# Test socket.if_indextoname

def check_buffsize():
    buf = []
    for i in range(100):
        for j in range(100):
            try:
                ifname = socket.if_indextoname(j)
            except ValueError:
                continue
            if ifname in buf:
                print('ERROR: duplicate interface name %s' % ifname)
            if j >= len(buf):
                buf.append(ifname)
            else:
                buf[j] = ifname

if __name__ == '__main__':
    check_buffsize()
