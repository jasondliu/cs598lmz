import sys, threading

def run():
    while True:
        try:
            print("running")
            time.sleep(1)
        except KeyboardInterrupt:
            print("exiting")
            sys.exit(0)

t = threading.Thread(target=run)
t.start()
