import sys, threading

def run():
    for i in range(5):
        print("Python")

t = threading.Thread(target=run)
t.start()

for i in range(5):
    print("Main")

t.join()
