import sys, threading

def run():
    print("run")
    sys.exit()

t = threading.Thread(target=run)
t.start()

# wait for thread to finish
t.join()

print("thread finished")
</code>
Output:
<code>run
thread finished
</code>

