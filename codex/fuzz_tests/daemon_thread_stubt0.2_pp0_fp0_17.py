import sys, threading

def run():
    while True:
        print("threading is running...")
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.start()
    while True:
        print("main threading is running...")
        time.sleep(1)

if __name__ == "__main__":
    main()
