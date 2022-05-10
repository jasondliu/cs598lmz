import sys, threading

def run():
    while True:
        print("Hello")

if __name__ == '__main__':
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
</code>
I'm running this code on a Raspberry Pi 3.
I've tried to use <code>thread.daemon = True</code> but it doesn't work.
I've also tried to use <code>thread.setDaemon(True)</code> but it doesn't work.
I've also tried to use <code>thread.setDaemon(True)</code> and <code>thread.join()</code> but it doesn't work.
I've also tried to use <code>thread.setDaemon(True)</code> and <code>thread.join(0)</code> but it doesn't work.
I've also tried to use <code>thread.setDaemon(True)</code> and <code>thread.join(1)</code> but it doesn't work.
I've also tried to use <code>thread.setDaemon(True)</code> and <code>thread.join(2
