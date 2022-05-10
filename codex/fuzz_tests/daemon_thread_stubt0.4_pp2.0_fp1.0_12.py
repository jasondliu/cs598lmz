import sys, threading

def run():
    while True:
        try:
            print(f"{threading.current_thread().name} is running")
            time.sleep(1)
        except KeyboardInterrupt:
            print(f"{threading.current_thread().name} is interrupted")
            sys.exit()

def main():
    t = threading.Thread(target=run, name="thread-1")
    t.start()
    t.join()

if __name__ == "__main__":
    main()
