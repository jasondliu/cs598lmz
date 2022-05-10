import sys, threading

def run():
    for i in range(10):
        print(i)
        time.sleep(1)

try:
    threading.Thread(target=run).start()
except:
    print("Error: unable to start thread")

while 1:
    pass
