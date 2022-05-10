import sys, threading
threading.Thread(target=lambda: sys.stdout.write("thread1\n")).start()
threading.Thread(target=lambda: sys.stdout.write("thread2\n")).start()
</code>
The outputs are non-deterministic (sometimes <code>thread1thread2</code>, sometimes <code>thread2thread1</code>), but the output ends without <code>\n</code> only <code>thread1thread2</code>. It is because <code>sys.stdout</code> is line-buffered and the second thread flushes the last <code>\n</code>.

