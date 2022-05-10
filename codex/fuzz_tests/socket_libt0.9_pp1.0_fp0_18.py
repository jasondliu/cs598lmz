import socket, fcntl, struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = get_ip_address('wlan0')
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print 'Connected with ' + host + ':' + str(port)

while 1:
    # message = raw_input("-> ")
    client_socket.sendall('sendback')
    data = client_socket.recv(4096)
    print(data)

client_socket.
