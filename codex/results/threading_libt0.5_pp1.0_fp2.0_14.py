import threading
threading.stack_size(67108864)


def run_task():
    # print('{} is running'.format(threading.current_thread().name))
    # time.sleep(2)
    # print('{} is done'.format(threading.current_thread().name))
    print('Thread {} is running'.format(threading.current_thread().name))
    n = 0
    while n < 5:
        n += 1
        print('Thread {} >>> {}'.format(threading.current_thread().name, n))
        time.sleep(1)
    print('Thread {} ended'.format(threading.current_thread().name))


if __name__ == '__main__':
    print('{} is running'.format(threading.current_thread().name))
    t = threading.Thread(target=run_task, name='MyThread')
    t.start()
    t.join()
    print('{} is done'.format(threading.current_thread().name))
