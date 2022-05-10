import sys, threading

def run():
    while True:
        print("Hello")

thread = threading.Thread(target=run)
thread.start()

while True:
    print("World")
</code>
I would expect the output to be:
<code>Hello
World
Hello
World
Hello
World
...
</code>
But instead I get:
<code>World
Hello
World
Hello
World
Hello
...
</code>
Why is this?


A:

This is because the <code>print</code> function is not thread-safe.
The <code>print</code> function is implemented in C and it uses a global lock to ensure that only one thread can print at a time.
If you want to print from multiple threads, you need to use a thread-safe print function.

