import sys, threading

def run():
    print("run")
    sys.exit()

def main():
    print("main")
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
    print("main end")

if __name__ == "__main__":
    main()
