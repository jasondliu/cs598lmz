import sys, threading

def run():
    while True:
        print("thread : %s" % threading.current_thread())
        time.sleep(1)

def main():
    # print("main : %s" % threading.current_thread())
    # t = threading.Thread(target=run)
    # t.start()
    # t.join()

    for i in range(5):
        t = threading.Thread(target=run)
        t.start()

if __name__ == '__main__':
    main()
