import sys, threading

def run():
    print("run")
    time.sleep(1)
    print("run2")

def main():
    print("main")
    t = threading.Thread(target=run)
    t.start()
    print("main2")

if __name__ == "__main__":
    main()
