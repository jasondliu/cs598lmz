import sys, threading

def run():
    print('Hello from thread %s' % threading.currentThread().getName())

def main():
    print('Hello from thread %s' % threading.currentThread().getName())
    sys.stdout.flush()

    t = threading.Thread(target=run, name='my_thread')
    t.start()

    print('Hello again from thread %s' % threading.currentThread().getName())
    sys.stdout.flush()

if __name__ == '__main__':
    main()
</code>
Output:
<code>Hello from thread MainThread
Hello again from thread MainThread
Hello from thread my_thread
</code>

