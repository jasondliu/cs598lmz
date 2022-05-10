import sys, threading

def run():
    print("run")

def main():
    threading.Timer(3.0, run).start()
    while 1:
        pass

if __name__ == "__main__":
    main()
