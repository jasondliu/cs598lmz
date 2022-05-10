import sys, threading

def run():
    for i in range(50):
        print("Hello")

t = threading.Thread(target=run)
t.start()

for i in range(50):
    print("Goodbye")
</code>
I would like the output to be:
<code>Hello
Goodbye
Hello
Goodbye
Hello
Goodbye
...
</code>
But instead, I get:
<code>Hello
Hello
Hello
Hello
Hello
Hello
...
Goodbye
Goodbye
Goodbye
Goodbye
Goodbye
Goodbye
...
</code>
I understand that this is because the thread is running the <code>for</code> loop before the main thread runs its <code>for</code> loop. But how can I get the output I want?


A:

You could use <code>asyncio</code> and <code>async</code>/<code>await</code> to achieve this:
<code>import asyncio

async def run():
    for i in range(50):
        print("Hello")

async def main():

