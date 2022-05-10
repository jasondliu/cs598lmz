import sys, threading

def run():
    while True:
        print("running")
        time.sleep(1)

t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

while True:
    print("main")
