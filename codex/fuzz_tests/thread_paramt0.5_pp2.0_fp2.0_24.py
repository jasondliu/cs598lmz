import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\n'.join(map(str,range(100000)))))
</code>
The above code will run in the background and print out 100,000 numbers. 

