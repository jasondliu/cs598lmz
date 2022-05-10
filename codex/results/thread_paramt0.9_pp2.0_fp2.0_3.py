import sys, threading
threading.Thread(target=lambda: sys.stdout.write('abcdefg\\n')).start()'
</code>
However, if there is only one source of input in the script, it works fine. Any clues what I can do in that case?


A:

Use the following syntax:
<code>!python -u -c 'for i in xrange(5): print i; sleep(.5); print i' | awk 'NR%2==1'
</code>

