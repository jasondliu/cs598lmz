import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()
</code>
This will read from <code>stdin</code> and write to <code>stdout</code> in another thread, so the <code>main</code> thread can continue to run the program.

