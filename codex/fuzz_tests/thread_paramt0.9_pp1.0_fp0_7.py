import sys, threading
threading.Thread(target=lambda: sys.stdout.write('red\n')).start()
sys.stdout.write('blue\n')

a = 1
def hello():
    global a
    a = 2
    print(a)

if __name__ == "__main__":
    print(a)
    hello()
    print(a)
