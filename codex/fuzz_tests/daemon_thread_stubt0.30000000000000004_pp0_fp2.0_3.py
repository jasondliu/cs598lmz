import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

# wait for the user to press enter
raw_input("Press enter to stop.")
thread.stop()
</code>

