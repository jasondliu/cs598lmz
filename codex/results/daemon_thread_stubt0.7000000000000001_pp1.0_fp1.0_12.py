import sys, threading

def run():
    print(sys.argv[1:])
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    sys.exit(0)

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
