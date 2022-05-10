import sys, threading
threading.Thread(target=lambda: sys.stderr.write("my stderr\n")).start()
print("my stdout\n")
</code>
Output:
<code>$ python -u ./pythonstderr.py
my stderr
my stdout
</code>
However, it's in your control which streams you write to. You're not required to write to stderr if you can write to stdout just as well. 

