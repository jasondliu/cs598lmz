import sys, threading

def run():
    for i in range(10000):
        print(i)

if __name__ == "__main__":
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
    print("Done")
