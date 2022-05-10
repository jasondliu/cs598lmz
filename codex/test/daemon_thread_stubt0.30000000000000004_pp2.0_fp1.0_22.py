import sys, threading

def run():
    print("run")
    sys.exit()

t = threading.Thread(target=run)
t.start()

while True:
    print("main")
