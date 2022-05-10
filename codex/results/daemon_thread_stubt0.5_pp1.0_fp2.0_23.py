import sys, threading

def run():
    print("called")
    sys.exit()

threading.Thread(target=run).start()

print("started")
</code>
Output:
<code>started
called
</code>

