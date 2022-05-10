import sys, threading

def run():
    for i in range(1, 500):
        print(threading.current_thread().getName() + " " + str(i))

if __name__ == "__main__":

    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done")
