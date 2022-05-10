import sys, threading

def run():
    print "hello"

def main():
    t = threading.Thread(target=run)
    t.start()

if __name__ == "__main__":
    main()
