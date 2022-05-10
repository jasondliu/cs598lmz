import sys, threading

def run():
    print("run")
    sys.exit()

def main():
    print("main")
    threading.Thread(target=run).start()
    print("main")

if __name__ == "__main__":
    main()
