import sys, threading

def run():
    while True:
        print("threading is running...")
        time.sleep(1)

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()
    print("main threading is running...")
    t.join()
    print("threading end")
