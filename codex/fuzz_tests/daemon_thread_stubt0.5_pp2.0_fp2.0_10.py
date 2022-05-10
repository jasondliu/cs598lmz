import sys, threading

def run():
    global running
    global s
    global data
    global address
    global port
    global lock
    global socket_list
    global index
    global data_list
    global address_list
    global port_list

    while running:
        try:
            data, address = s.recvfrom(1024)
            port = address[1]
            lock.acquire()
            socket_list.append(s)
            data_list.append(data)
            address_list.append(address)
            port_list.append(port)
            lock.release()
        except:
            pass

def process():
    global running
    global s
    global data
    global address
    global port
    global lock
    global socket_list
    global index
    global data_list
    global address_list
    global port_list

    while running:
        try:
            lock.acquire()
            if len(socket_list) > 0:
                s = socket_list[0]
                data = data_list[0]
                address = address_list[
