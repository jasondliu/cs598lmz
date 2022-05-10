import threading
threading.stack_size(67108864)

def main():
    print('main')
    t = threading.Thread(target=func, args=(10,))
    t.start()
    t.join()

def func(num):
    print('func')
    print(sum(i*i for i in range(num)))

main()
