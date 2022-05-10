import signal
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

group = 1
clients = 0
connections = []
order = ''

def new_connections(con):
    global connections,clients,order
    fd, addr = con.accept()
    connections.append(fd)
    fd.send("Enter name: ")
    name = fd.recv(1024)
    if name == "admin" :
        new_chat_group(fd)
    else:
        clients += 1
        if clients == group:
            order = 'start'
            for con in connections:
                con.send("Start game")
            prepare(fd,name)
        else:
            prepare(fd,name)

def new_chat_group(con):
    global group,clients,connections
    con.send('Enter group size :')
    group = int(con.recv(1024))
    clients = 0
    con.send('Enter new order id :')
    order = con.recv(1024)
    con
