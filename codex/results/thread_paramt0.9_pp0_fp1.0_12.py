import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello world!\n')).start()
</code>

<code>subprocess</code> module (2.6+):
<code>import subprocess
subprocess.Popen(['python', '-c', 'import sys, time\ntime.sleep(.1); sys.stdout.write("Hello world!\\n")'])
</code>

