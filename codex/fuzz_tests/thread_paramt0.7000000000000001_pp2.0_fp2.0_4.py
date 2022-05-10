import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
</code>
In Windows, you can use the <code>subprocess</code> module:
<code>import subprocess
subprocess.Popen("python -c 'import sys, time; sys.stdout.write(\"hello\\n\"); time.sleep(5)'", shell=True)
</code>

