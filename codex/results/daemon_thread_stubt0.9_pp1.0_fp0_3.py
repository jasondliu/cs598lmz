import sys, threading

def run():
    print('Client Started')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('0.0.0.0', 12345))
    while 1:
        sRecv=s.recv(256)
        print('receive "%s"' % sRecv)
        if sRecv!='OK':
            break
        
        s.send('this is 
