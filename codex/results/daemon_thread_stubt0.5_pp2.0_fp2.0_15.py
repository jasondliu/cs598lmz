import sys, threading

def run():
    while True:
        print("Hello World!")

if __name__ == '__main__':
    threading.Thread(target=run).start()
    sys.exit(0)
