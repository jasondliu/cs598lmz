import sys, threading

def run():
    for i in range(1,100):
        print(i)
        time.sleep(0.1)

def main():
    print("start")
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
    print("end")

if __name__ == '__main__':
    main()
