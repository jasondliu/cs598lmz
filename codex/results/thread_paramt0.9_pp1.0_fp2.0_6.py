import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Do some stuff\n")).start()
print("testing")
sys.stdout.flush()
</code>
Output:
<code>testing
Do some stuff
</code>

