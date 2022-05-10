import sys, threading

def run():
    for i in range(1000000):
        f1 = open("/home/jflinn/tmp/testlock1", "r+")
        fcntl.flock(f1, fcntl.LOCK_EX)
        f1.write("johndoe\n")
        f1.close()

if __name__ == '__main__':
    threads = []
    for i in range(100):
        t = threading.Thread(target=run, name="thread"+str(i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
