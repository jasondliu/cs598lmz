import sys, threading

def run():
    for i in range(100):
        print(i)

threading.Thread(target=run).start()

for i in range(100):
    print(i)
