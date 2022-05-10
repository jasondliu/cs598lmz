import sys, threading

def run():
    print("current threading {}".format(threading.current_thread().name))

    for i in range(100):
        print("{}: {}".format(threading.current_thread().name, i))

if __name__ == "__main__":
    all_thread = []
    for i in range(100):
        t = threading.Thread(target=run)
        t.start()
        all_thread.append(t)

    for t in all_thread:
        t.join()
