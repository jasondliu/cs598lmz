import sys, threading

def run():
    print("run")
    time.sleep(1)
    print("run end")

def main():
    print("main")
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print("main end")

if __name__ == "__main__":
    main()
