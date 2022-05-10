import sys, threading

def run():
    print "Thread1"
    print "Thread2"

def main():
    threading.Thread(target=run).start()
    time.sleep(0.1)
    print "Main"

main()
</code>
Output:
<code>Thread1
Thread2
Main
</code>
Why does the <code>main</code> function print before the <code>run</code> function? I expected the output to be:
<code>Thread1
Thread2
Main
</code>
I am using Python 2.7.6 on OS X 10.10.2.

