import sys, threading

def run():
    for i in range(5):
        print(i)
        time.sleep(1)

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread.start()
    print("Started")
    time.sleep(3)
    thread.join()
    print("Done")
