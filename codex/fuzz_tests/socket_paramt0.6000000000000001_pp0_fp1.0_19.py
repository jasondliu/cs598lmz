import socket
socket.if_indextoname('2')

#this is the main loop
while True:
    try:
        time.sleep(1)
        #check if the network is up
        if(os.system("ping -c 1 8.8.8.8") == 0):
            net = True
            print("the net is up")
        else:
            net = False
            print("the net is down")
        #if the net is up and the server is down, try to start the server
        if(net == True and server == False):
            print("starting the server")
            os.system("sudo /etc/init.d/ssh start")
            if(os.system("ping -c 1 192.168.1.10") == 0):
                server = True
                print("server started")
            else:
                server = False
                print("server not started")
        #if the net is up and the server is up, check if the wifi is connected
        if(net == True and server == True):
            print("checking wifi")
            if(os.system("ping -c 1 192.168.1.
