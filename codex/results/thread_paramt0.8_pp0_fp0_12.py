import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hi!\n")).start()
</code>
What's the difference? ^^


A:

You can't do anything else if stdout is being redirected. If you're redirecting stdout to a file in a thread, it also means that any stdout in other threads is also redirected to that file.
If you're redirecting stdout in a thread and you want to print something in another thread without affecting the redirect, you'd have to save the old value of sys.stout and restore it while printing.

