import sys, threading
threading.Thread(target=lambda: sys.stdout.write('{}'.format(code)),args=(), daemon=True).start(); main('')
</code>
Wonder if anyone can explain why this works.
Thanks in advance.

