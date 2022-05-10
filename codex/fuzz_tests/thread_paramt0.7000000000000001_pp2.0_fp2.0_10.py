import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(sys.argv[1:]))).start()
</code>
I can't work out where the <code>\n</code> is coming from.


A:

The <code>\n</code> is not coming from the script you posted.
The problem was likely that you were running the script in an interactive terminal, and you probably had an empty command line after running the script. The <code>\n</code> then came from the terminal.
This is easy to reproduce:
<code>$ cat test.py 
#!/usr/bin/env python3
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(sys.argv[1:]))).start()
$ echo -e 'test1\ntest2\ntest3' | ./test.py
$ # the cursor is on a new line here
</code>

