import sys, threading

def run():
    print("run")
    time.sleep(1)


class ThreadTest(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID

    def run(self):
        print("run")
        time.sleep(1)

def main():
    for i in range(10):
        thread = ThreadTest(i)
        thread.start()
        thread.join()


if __name__ == "__main__":
    main()
