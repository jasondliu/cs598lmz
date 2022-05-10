import socket
socket.if_indextoname()

if socket.has_ipv6 == True :
    
    try:
        s.bind((interface_ip, interface_port))
        print("Listening on {}:{}".format(interface_ip, interface_port))
    except OSError as e:
        print("Unable to bind on {}:{}, error:{}".format(interface_ip, interface_port, e.args[1]))
    
    
    while True:
        t = time.time()
        data, source = s.recvfrom(1024)
        elapsed = time.time() - t
        print("Received {} bytes from {}:{}: {}".format(len(data), source[0], source[1], data.decode('utf-8')))
        print("Elapsed time: {:.2f} seconds".format(elapsed))
        
    s.close()

else:
    print("IPv6 is not enabled")
