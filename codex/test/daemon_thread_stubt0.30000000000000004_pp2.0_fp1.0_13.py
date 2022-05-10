import sys, threading

def run():
    print("running")
    sys.stdout.flush()
    time.sleep(1)

def main():
    for i in range(5):
        threading.Thread(target=run).start()

if __name__ == "__main__":
    main()
