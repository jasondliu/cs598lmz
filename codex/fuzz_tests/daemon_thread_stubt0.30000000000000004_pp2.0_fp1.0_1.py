import sys, threading

def run():
    print("threading")
    sys.stdout.flush()
    time.sleep(2)

def main():
    print("main")
    sys.stdout.flush()
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
    print("main end")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
