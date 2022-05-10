import sys, threading

def run():
    while True:
        print("hello")
        sys.stdout.flush()

t = threading.Thread(target=run)
t.start()

while True:
    print("world")
    sys.stdout.flush()
</code>
I have tried:
<code>sys.stdout.flush()
sys.stdout.write("\n")
</code>
I have also tried to flush the output of the run function but I am not sure how to do that.
Here is the output:
<code>world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world
hello
world
world

