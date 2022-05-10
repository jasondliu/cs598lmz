import sys, threading

def run():
    while True:
        time.sleep(2)
        print(datetime.datetime.now())

def main():
    t = threading.Thread(target=run)
    t.setDaemon(True) # set Daemon
    t.start()

    print("start")
    time.sleep(10)
    print("end")

if __name__ == "__main__":
    main()
