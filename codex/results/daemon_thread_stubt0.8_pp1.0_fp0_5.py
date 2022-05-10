import sys, threading

def run():
    for i in range(1, 100):
        print(i)
        time.sleep(0.01)

def main():
    threading.Thread(target=run, name='th1', args=()).start()
    threading.Thread(target=run, name='th2', args=()).start()

if __name__ == "__main__":
    main()
