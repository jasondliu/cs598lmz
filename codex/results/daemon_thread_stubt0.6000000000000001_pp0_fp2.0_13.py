import sys, threading

def run():
    i=0
    while True:
        print(i)
        i+=1

t = threading.Thread(target=run)
t.start()

while True:
    time.sleep(0.1)
    print("Main")
    t.join()
