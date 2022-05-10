import sys, threading

def run():
    while True:
        try:
            print("running")
            time.sleep(1)
        except KeyboardInterrupt:
            print("keyboard interrupt")
            break

def main():
    t1 = threading.Thread(target=run)
    t1.start()
    t1.join()

if __name__ == "__main__":
    main()
