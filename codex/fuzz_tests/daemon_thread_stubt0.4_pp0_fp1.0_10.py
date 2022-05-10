import sys, threading

def run():
    for i in range(10):
        print("Hello")
        time.sleep(1)

threading.Thread(target=run).start()

while True:
    pass
