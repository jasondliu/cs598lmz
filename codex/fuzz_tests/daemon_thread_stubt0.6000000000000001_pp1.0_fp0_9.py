import sys, threading

def run():
    while 1:
        print('thread running')
        sleep(1)

def main():
    t = threading.Thread(target=run)
    t.start()
    while 1:
        print('main running')
        sleep(1)

if __name__ == '__main__':
    main()
</code>
The output is:
<code>main running
thread running
main running
thread running
</code>
It seems that the thread is started and run properly.
I have also tried to run the same code in a script file, the output is the same.
I think the thread is not running in parallel, because the output is the same as the one in single thread.
I am using python3.3 and my OS is windows7.
I have also tried the code in a linux system, the result is the same.
So, is there something wrong with my code? 


A:

This depends on the implementation of the Python interpreter, but in CPython, the main thread is the only thread that can access the Python interpreter. So, the main thread is the only thread that can run Python code.
