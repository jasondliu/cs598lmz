import sys, threading

def run():

    sys.stdin = open('/dev/tty')
    while True:
        try:
           exec(sys.stdin.readline())
        except:
           pass

t = threading.Thread(target=run)
t.daemon = True
t.start()
