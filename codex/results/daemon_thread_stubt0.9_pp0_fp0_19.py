import sys, threading

def run():
    ip ="0.0.0.0"
    bind_ip = ip
    bind_port = 9999
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip,bind_port))
    server.listen(5)  # max backlog of connections
    print ('Listening on {}:{}'.format(bind_ip, bind_port))
    client_sock, address = server.accept()
    data = client_sock.recv(4096)
    print(data)

t1 = threading.Thread(target=run)      
t1.daemon = True
t1.start()

def get_route_ip(route):
    return ipcalc.Network(route).network()

def get_route_broadcast(route):
    return ipcalc.Network(route).broadcast()

def get_route_gw(route):
    return route.split()[1]

def root_call(command):
    output = subprocess.Popen(command
