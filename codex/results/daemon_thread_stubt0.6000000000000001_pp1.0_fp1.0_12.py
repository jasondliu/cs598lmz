import sys, threading

def run():
    print("I am running")
    sys.exit(1)


if  __name__ == "__main__":
    t = threading.Thread(target=run)
    t.start()
    print("I am main")
