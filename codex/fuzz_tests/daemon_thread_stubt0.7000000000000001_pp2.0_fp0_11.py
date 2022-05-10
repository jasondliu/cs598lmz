import sys, threading

def run():
    print("I'm a thread!")
    sys.stdout.flush()

t = threading.Thread(target=run)
t.start()

print("I'm the main thread!")
sys.stdout.flush()
t.join()
</code>
When I run this script, I get the following output:
<code>I'm the main thread!
I'm a thread!
</code>
I'd like to understand why the output is not always in the same order. Sometimes I get the first line from the main thread, and sometimes from the secondary thread.
What's causing this?


A:

Because you're using threads, the operating system schedules which thread runs at what time. The output order that you see depends on the time the operating system chooses for each thread.
In other words, you're asking why the first print statement comes out after the second, but the operating system is not required to print the first print statement before the second.

