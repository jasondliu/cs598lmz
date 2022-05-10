import sys, threading

def run():
    print("Threading")
    for i in range(0, 10):
        print("Threading")
    return

t = threading.Thread(target=run)
t.start()
