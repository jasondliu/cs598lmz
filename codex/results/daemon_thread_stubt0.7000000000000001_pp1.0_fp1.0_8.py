import sys, threading

def run():
    for i in range(0,300):
        print(i)

for i in range(0,4):
    threading.Thread(target=run).start()
