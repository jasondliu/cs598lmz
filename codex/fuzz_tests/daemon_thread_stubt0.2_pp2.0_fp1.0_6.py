import sys, threading

def run():
    for i in range(1, 100):
        print(i)

threading.Thread(target=run).start()

while True:
    print("main")
    time.sleep(1)
