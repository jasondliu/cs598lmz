import sys, threading

def run():
    i = 0
    while True:
        time.sleep(1)
        i += 1
        print i

def main():
    t = threading.Thread(target=run)
    t.start()

if __name__ == "__main__":
    main()
