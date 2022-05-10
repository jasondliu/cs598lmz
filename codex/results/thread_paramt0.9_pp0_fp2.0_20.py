import sys, threading
threading.Thread(target=lambda: sys.stdout.write('ABC')).start()
sys.stdout.write('DEF')
</code>
prints any of <code>ABCDEF</code>, <code>DEFABC</code>, <code>ABC</code>, and <code>DEF</code>, as far as I know. Any ideas?


A:

This is one of Python's curses.  The GIL (global interpreter lock) in Python ensures that only one thread is ever running Python code at once. Instead of using Python's built-in threads, you may want to look into using Pyrex or something similar to write native threads.

