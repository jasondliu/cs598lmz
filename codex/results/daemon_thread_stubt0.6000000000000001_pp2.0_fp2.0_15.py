import sys, threading

def run():
    sys.stdout.write("thread started\n")
    sys.stdout.write("thread ended\n")

if __name__ == "__main__":
    sys.stdout.write("main started\n")
    t = threading.Thread(target=run)
    t.start()
    t.join()
    sys.stdout.write("main ended\n")
