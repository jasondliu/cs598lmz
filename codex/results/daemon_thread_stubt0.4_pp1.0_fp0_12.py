import sys, threading

def run():
    while True:
        print "hello"

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()

    while True:
        pass
