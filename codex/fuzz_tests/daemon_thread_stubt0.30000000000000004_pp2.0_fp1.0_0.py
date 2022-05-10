import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

while True:
    print("World")
    time.sleep(1)
</code>
I have tried to use <code>thread.join()</code> but it doesn't work.
I have also tried to use <code>thread.isAlive()</code> but it doesn't work either.
I have tried to use <code>thread.is_alive()</code> but it doesn't work either.
I have tried to use <code>thread.is_daemon()</code> but it doesn't work either.
I have tried to use <code>thread.is_set()</code> but it doesn't work either.
I have tried to use <code>thread.is_stopped()</code> but it doesn't work either.
I have tried to use <code>thread.is_started()</code> but it doesn't work either.
I have tried to use <code>thread.is_
