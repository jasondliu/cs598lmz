import threading
threading.stack_size(67108864)

def func():
    print('thread function')
    time.sleep(1)
    print('thread function end')

if __name__ == '__main__':
    t = threading.Thread(target=func)
    t.start()
    t.join()
    print('main thread end')
</code>
I use windows 10 and python 3.6.5.
I have also tried with python 2.7.15 and had the same issue.
I have also tried with python 3.7.2 and had the same issue.
I have also tried to get the stack size with the following code:
<code>import threading
print(threading.stack_size())
</code>
and I got 0.
I have also tried to set the stack size with the following code:
<code>import threading
threading.stack_size(67108864)
</code>
and I got the following error:
<code>Traceback (most recent call last):
  File "C:\Users\jeanbaptiste\Desktop\test
