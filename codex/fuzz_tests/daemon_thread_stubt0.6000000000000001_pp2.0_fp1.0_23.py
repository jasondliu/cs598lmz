import sys, threading

def run():
    with open('1.txt', 'r') as f:
        data = f.read()
    print(data)

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()
</code>
I'm trying to read a file in a thread. The file is a .txt file with a lot of data.
If I run this script I get a error:
<code>IOError: [Errno 32] Broken pipe
</code>
I'm using Python 2.6.5
I'm a newbie in Python, I didn't find anything about this error with my version of Python.
Thanks in advance.


A:

The error is because you are ending the program before the thread has had a chance to do anything.
Try
<code>t.join()
</code>
after t.start()

