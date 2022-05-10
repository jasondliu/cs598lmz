import sys, threading

def run():
    while(True):
        print("Hello")
        time.sleep(1)

def main():
    t=threading.Thread(target=run)
    t.setDaemon(True)
    t.start()

    while True:
        print("Main")
        time.sleep(1)

if __name__=="__main__":
    main()
