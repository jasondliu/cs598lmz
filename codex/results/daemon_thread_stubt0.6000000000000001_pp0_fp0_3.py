import sys, threading

def run():
    for i in range(10000):
        print(i)

threading.Thread(target=run).start()
</code>

