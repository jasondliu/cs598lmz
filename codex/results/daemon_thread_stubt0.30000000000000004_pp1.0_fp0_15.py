import sys, threading

def run():
    while True:
        print("Hello")

def main():
    t = threading.Thread(target=run)
    t.start()

if __name__ == "__main__":
    main()
</code>
I would like to be able to run this script and have the "Hello" print out every second, but I would also like to be able to send a signal to the script to stop the thread.
I've tried using the signal module, but I can't seem to get it to work.
<code>import sys, threading, signal

def run():
    while True:
        print("Hello")

def main():
    t = threading.Thread(target=run)
    t.start()
    signal.signal(signal.SIGINT, t.stop)

if __name__ == "__main__":
    main()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    main()
  File "test.py
