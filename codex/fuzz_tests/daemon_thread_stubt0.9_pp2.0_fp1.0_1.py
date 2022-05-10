import sys, threading

def run():
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(('192.168.10.17', 514))
    while True:
        message = raw_input("log message: ")
        message = "[" + getpass.getuser() + "] " + message
        data = "[{ \"log_at\": \"" + str(datetime.datetime.now()) + "\", \"message\": \"" + message + "\" }]\n"
        try:
            tcpCliSock.send(data)
            data = tcpCliSock.recv(1024)
        except EOFError as e:
            print "Connection error."
            break
    tcpCliSock.close()

RUN = True

def start_logging(event):
    global RUN
    t = threading.Thread(target=run)
    t.start()
    RUN = True
    event.is_set()

def stop_logging(event):
    global RUN
    RUN = False
    event
