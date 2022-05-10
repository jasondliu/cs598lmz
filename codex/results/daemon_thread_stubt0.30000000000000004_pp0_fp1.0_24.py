import sys, threading

def run():
    print("run")
    sys.stdout.flush()
    time.sleep(1)
    print("done")
    sys.stdout.flush()

def main():
    print("main")
    sys.stdout.flush()
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print("main done")
    sys.stdout.flush()

main()
