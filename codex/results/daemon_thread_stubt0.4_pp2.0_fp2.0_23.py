import sys, threading

def run():
    print("I'm in thread:", threading.current_thread().name)
    sys.stdout.flush()

def main():
    print("I'm in thread:", threading.current_thread().name)
    sys.stdout.flush()

    t = threading.Thread(target=run, name="my_thread")
    t.start()
    t.join()

if __name__ == "__main__":
    main()
