import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

for i in range(5):
    t = threading.Thread(target=run)
    t.start()
