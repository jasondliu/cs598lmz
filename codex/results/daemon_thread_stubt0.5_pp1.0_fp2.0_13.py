import sys, threading

def run():
    print("start")
    for i in range(5):
        print("running")

t = threading.Thread(target=run)
t.start()

while True:
    print("main")
