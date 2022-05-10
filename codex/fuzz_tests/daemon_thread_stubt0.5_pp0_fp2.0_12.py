import sys, threading

def run():
    print(socket.gethostbyname(socket.gethostname()))
    sys.stdout.flush()
    threading.Timer(1.0, run).start()

run()
