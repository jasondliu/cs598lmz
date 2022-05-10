import sys, threading

def run():
    while True:
        print("Hello")

def main():
    thread = threading.Thread(target=run)
    thread.start()

    while True:
        print("World")

if __name__ == "__main__":
    main()
</code>
I would expect the output to be:
<code>Hello
World
Hello
World
...
</code>
But the actual output is:
<code>World
Hello
World
Hello
...
</code>
Why is that?


A:

The output is not guaranteed to be in any particular order.
The two threads can run in any order, and the output from each thread can be interleaved in any order.

