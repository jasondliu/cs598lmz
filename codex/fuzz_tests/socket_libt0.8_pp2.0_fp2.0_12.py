import socket
import subprocess
import sys

if __name__=="__main__":
    if len(sys.argv) < 2:
        print "Usage: ./server <port>\n"
        sys.exit(1)
        
    if len(sys.argv) == 3:
        debug = 1
    else:
        debug = 0
    
    port = int(sys.argv[1])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', port))
    
    if debug:
        print "Listening on port %s...\n" % sys.argv[1]
    
    while 1:
        try:
            data, addr = sock.recvfrom(1024)
            print "Received message: '%s' from %s\n" % (data, addr)
            cmd = data.split()
            ret = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            out, err = ret.communicate()
           
