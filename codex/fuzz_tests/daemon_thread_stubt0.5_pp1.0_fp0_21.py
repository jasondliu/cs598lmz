import sys, threading

def run():
    while True:
        time.sleep(1)
        print("I'm running")

t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

while True:
    time.sleep(1)
    print("I'm main")

print("Done")
