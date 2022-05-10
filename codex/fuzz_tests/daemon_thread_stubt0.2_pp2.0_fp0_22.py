import sys, threading

def run():
    print("run")
    sys.stdout.flush()
    time.sleep(1)

def main():
    print("main")
    sys.stdout.flush()
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
    print("main")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
