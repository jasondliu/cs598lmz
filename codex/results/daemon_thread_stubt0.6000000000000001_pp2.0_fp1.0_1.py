import sys, threading

def run():
    for i in range(1, 1000000):
        print(i)
        time.sleep(0.01)
    
if __name__ == '__main__':
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
