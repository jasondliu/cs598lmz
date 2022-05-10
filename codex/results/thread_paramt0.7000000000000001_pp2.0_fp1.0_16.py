import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread\n')).start()
print('main')
</code>
will print
<code>main
thread
</code>
If you want to make sure that <code>thread</code> is printed first, the only way to ensure that is by having the main thread wait for the thread to finish.
You can do that by putting the thread in a daemon:
<code>import threading
threading.Thread(target=lambda: sys.stdout.write('thread\n'), daemon=True).start()
print('main')
</code>
will print
<code>thread
main
</code>
Note that because the threads are running in parallel, there's no guarantee that <code>thread</code> will be printed before <code>main</code> (although it's more likely because of the way <code>print</code> flushes).

