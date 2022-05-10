import sys, threading

def run():
    print(threading.current_thread().getName() + ": start")
    sys.exit(1)
    print(threading.current_thread().getName() + ": stop")

if __name__ == "__main__":
    while True:
        t = threading.Thread(target=run)
        t.start()
