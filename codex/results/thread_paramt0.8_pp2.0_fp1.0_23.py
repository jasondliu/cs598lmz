import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.readline())).start()
</code>
Then in the python3 debugger process I use the following command:
<code>run -i test.py &lt; input.txt
</code>
This works for me.

