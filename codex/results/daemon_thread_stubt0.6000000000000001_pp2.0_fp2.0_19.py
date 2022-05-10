import sys, threading

def run():
    while True:
        print('test')

def main():
    threading.Thread(target = run).start()

if __name__ == '__main__':
    main()
</code>
The above script prints 'test' indefinetly.
I want to print 'test' for a certain amount of time, say 30 seconds.
So I've tried to add a <code>time.sleep(30)</code> in the <code>run()</code> function as follows:
<code>import time, sys, threading

def run():
    while True:
        print('test')
        time.sleep(30)

def main():
    threading.Thread(target = run).start()

if __name__ == '__main__':
    main()
</code>
The script now doesn't print anything, even though I've placed the <code>time.sleep()</code> in the <code>while</code> loop.
I know that I can add a <code>time.sleep(30)</code> to the end of the <code>run()</code> function,
