import sys, threading

def run():
    print "Hello"

if __name__ == "__main__":
    for i in range(5):
        threading.Thread(target=run).start()
