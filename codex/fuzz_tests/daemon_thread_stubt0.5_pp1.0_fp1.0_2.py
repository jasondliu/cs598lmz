import sys, threading

def run():
    print("hello")

if __name__=="__main__":
    threading.Timer(5.0, run).start()
    print("world")
    while True:
        pass
