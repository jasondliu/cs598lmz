import sys, threading

def run():
    while True:
        data=raw_input()
        if data=="quit":
            sys.exit(0)
        print data

t=threading.Thread(target=run)
t.daemon = True
t.start()

while True:
    data=raw_input()
    if data=="quit":
        sys.exit(0)
    print data
