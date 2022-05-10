import sys, threading

def run():
    for i in range(10):
        print(sys.argv[1], i)

threading.Thread(target=run, args=(sys.argv[1],)).start()
