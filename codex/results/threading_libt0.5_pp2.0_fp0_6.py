import threading
threading.stack_size(67108864)

def f(n):
    print(n)

if __name__ == '__main__':
    t = threading.Thread(target=f, args=(10,))
    t.start()
    t.join()
