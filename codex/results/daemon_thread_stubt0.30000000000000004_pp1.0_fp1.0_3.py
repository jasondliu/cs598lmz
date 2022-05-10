import sys, threading

def run():
    while True:
        print(threading.current_thread().name)
        time.sleep(1)

if __name__ == '__main__':
    threading.Thread(target=run, name='thread-1').start()
    threading.Thread(target=run, name='thread-2').start()
    threading.Thread(target=run, name='thread-3').start()
    threading.Thread(target=run, name='thread-4').start()
    threading.Thread(target=run, name='thread-5').start()
</code>
Output:
<code>thread-1
thread-1
thread-1
thread-1
thread-1
thread-2
thread-2
thread-2
thread-2
thread-2
thread-3
thread-3
thread-3
thread-3
thread-3
thread-4
thread-4
thread-4
thread-4
thread-4
thread-5
thread-5
thread-5
thread-5
thread-5
</code>

