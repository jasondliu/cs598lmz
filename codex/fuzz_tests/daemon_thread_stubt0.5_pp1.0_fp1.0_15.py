import sys, threading

def run():
    for i in range(10):
        print(i)

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()

    t.join()
    print('Thread finished')
