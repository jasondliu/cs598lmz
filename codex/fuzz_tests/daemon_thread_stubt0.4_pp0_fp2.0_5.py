import sys, threading

def run():
    print("Starting thread")
    time.sleep(3)
    print("Ending thread")

threading.Thread(target=run).start()

print("Main thread")
</code>
Output:
<code>Main thread
Starting thread
Ending thread
</code>

