import threading
threading.Thread(target=webserver).start()

tap0 = netifaces.ifaddresses('tap0')
myip = tap0[netifaces.AF_INET][0]['addr']

# Main loop
while True:
    print 'Ready'
    # Listen for incoming connections
    while True:
        # Wait for a connection
        print 'waiting for a connection'
        client, addr = s.accept()

        # Parse incomming data
        data = client.recv(1024)
        print data
        a=IP(data)
        #if a[IP].dst==self.ip:
        if a[IP].dst in myip:
            print 'ipv4'
            if a.haslayer(TCP):
                if a[TCP].flags == "S":
                    print 'tcp'
                    # Create a new packet to reply
                    b=IP(dst=a[IP].src,src=a[IP].dst)/TCP(dport=a[TCP].sport,sport=a[TCP
