import threading
# Test threading daemon

def print_daemon(name, n):
    print('\n'*n, '{} running'.format(name))
    print('{} ending'.format(name))


def print_thread(name):
    print('{} running'.format(name))
    print('{} ending'.format(name))

def main():
    d = threading.Thread(target=print_daemon, args=('daemon', 1), daemon=True)
    t = threading.Thread(target=print_thread, args=('thread',))
    d.start()
    t.start()
    print('main')

if __name__ == '__main__':
    main()

# main
# 
# daemon running
# daemon ending
# thread running
# thread ending
