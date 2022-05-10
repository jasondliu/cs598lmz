import sys, threading

def run():
    print("thread")

threading.Thread(target=run).start()

print("main")
</code>
outputs
<code>thread
main
</code>

