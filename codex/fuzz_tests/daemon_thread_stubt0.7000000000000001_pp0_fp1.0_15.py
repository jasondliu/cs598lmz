import sys, threading

def run():
    print("{}".format(threading.current_thread().getName()))
    print("{}".format(sys.version))

def main():
    print("{}".format(threading.current_thread().getName()))
    t = threading.Thread(target=run)
    t.start()

if __name__ == "__main__":
    main()
