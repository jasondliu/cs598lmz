import sys, threading

def run():
    global msg_1
    while 1:
        msg_1.set()

def run2():
    global msg_2
    while 1:
        if msg_1.is_set():
            print >>sys.stderr, '---'
            msg_1.clear()
            msg_2.set()

msg_1 = threading.Event()
msg_2 = threading.Event()

threading.Thread(target=run).start()
threading.Thread(target=run2).start()
