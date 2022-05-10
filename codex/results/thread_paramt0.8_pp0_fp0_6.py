import sys, threading
threading.Thread(target=lambda: sys.stderr.write('Hello world\n')).start()
</code>
It works with <code>multiprocessing.Process</code> and <code>threading.Thread</code>, but not with <code>concurrent.futures.ProcessPoolExecutor</code>.

