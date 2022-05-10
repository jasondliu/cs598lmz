import sys, threading

def run():
    while True:
        print("[*] thread running")
        time.sleep(5)

def main():
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()

    while True:
        print("[*] main running")
        time.sleep(5)

if __name__ == '__main__':
    main()
