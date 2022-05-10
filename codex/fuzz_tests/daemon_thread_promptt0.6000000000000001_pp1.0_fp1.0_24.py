import threading
# Test threading daemon thread.

def run():
    while True:
        print('I am running.')
        time.sleep(0.5)

t = threading.Thread(target=run, daemon=True)
t.start()
time.sleep(1)
t.join()

# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am running.
# I am
