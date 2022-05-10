import sys, threading

def run():
    while True:
        print("Hello")

def main():
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()

if __name__ == "__main__":
    main()
</code>
I want to run the <code>run()</code> function in a separate thread, but I want to wait for it to finish before exiting the program.
I've tried using <code>thread.join()</code> but it doesn't seem to work.
I've also tried using <code>thread.is_alive()</code> to check if the thread is still running, but it doesn't seem to work either.
I'm running this on Windows 10.
What am I doing wrong?


A:

The problem is that the <code>run</code> function never ends. You need to add a <code>break</code> statement somewhere in the loop.

