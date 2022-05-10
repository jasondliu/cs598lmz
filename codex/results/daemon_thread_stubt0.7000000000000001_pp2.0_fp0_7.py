import sys, threading

def run():
    while True:
        print("running")
        time.sleep(0.1)

t = threading.Thread(target=run)
t.start()

# ...

# wait for the thread to complete its work
t.join()
sys.exit(0)
</code>

