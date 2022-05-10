import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()
</code>
And then run the program like this:
<code>./a.out &lt; input.txt
</code>

