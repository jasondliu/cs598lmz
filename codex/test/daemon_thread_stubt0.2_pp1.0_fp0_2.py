import sys, threading

def run():
    print("run")
    for i in range(10):
        print(i)
        time.sleep(1)

def main():
    print("main")
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print("main end")

if __name__ == "__main__":
    main()
