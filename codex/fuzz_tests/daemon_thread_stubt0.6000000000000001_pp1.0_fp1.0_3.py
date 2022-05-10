import sys, threading

def run():
    for i in range(10000):
        print(i)

t = threading.Thread(target=run)
t.start()

sys.exit()
