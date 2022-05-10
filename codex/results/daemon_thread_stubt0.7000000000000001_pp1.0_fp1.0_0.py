import sys, threading

def run():
    print("test")
    sys.exit()

def main():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    t.join()

if __name__ == '__main__':
    main()
