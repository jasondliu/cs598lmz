import sys, threading

def run():
    print("thread start")
    sys.exit()
    print("thread end")

t = threading.Thread(target=run)
t.start()
t.join()

print("main end")
