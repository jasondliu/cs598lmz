import sys, threading

def run():
    for i in range(100000):
        print(i)
        sys.stdout.flush()


th = threading.Thread(target=run)
th.start()
th.join()
