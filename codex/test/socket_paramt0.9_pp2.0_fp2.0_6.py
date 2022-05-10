import socket
socket.if_indextoname(13)

def getAllNetCards():    
    nics = socket.if_nameindex()
    name2nic = {}
    for idx, name in nics:
        if idx > 0 and name.find("lo0") < 0:
            name2nic[name] = idx
    return name2nic

def getNetCardInfo():
    name2ip = {}
    stream = os.popen("ifconfig")
    while True:
        line = stream.readline()
        if not line:
            break
        if line.find('flags=') != -1:
            line = stream.readline().strip()
            if line.find('inet ') != -1:
                inet = line.split(' ')[1]
                ip_addr = inet.split(':')[1]
                name2ip[name] = ip_addr
        if line.find('#') != -1:
            name = line.split('#')[0]
    return name2ip

