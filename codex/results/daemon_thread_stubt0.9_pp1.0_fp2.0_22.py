import sys, threading

def run():
    global line
    if sys.argv[1] == '-s':
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((sys.argv[2], int(sys.argv[3])))
            line = '[%s] ' % str(s.getsockname())
            print('Connected to remote host. Start sending messages')
            threading._start_new_thread(send, (s,))
            threading._start_new_thread(receive, (s,))
        except:
            pass
        
    elif sys.argv[1] == '-c':
        HOST = input('Enter IP: ')
        PORT = input('Enter PORT: ')
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, int(PORT)))
            line = '[%s] ' % str(s.getsockname())
            print('Connected to remote host. Start sending
