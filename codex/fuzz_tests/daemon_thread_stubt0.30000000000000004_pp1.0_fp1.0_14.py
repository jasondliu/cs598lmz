import sys, threading

def run():
    while True:
        print("hello")

thread = threading.Thread(target=run)
thread.start()

while True:
    print("world")
</code>
I get this output:
<code>world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world
hello
world

