import sys, threading

def run():
    while True:
        print("Hello")

threading.Thread(target=run).start()

print("World")
</code>
I expect the output to be:
<code>World
Hello
Hello
Hello
Hello
Hello
...
</code>
But instead I get:
<code>World
Hello
Hello
Hello
Hello
Hello
...
Hello
Hello
Hello
Hello
Hello
...
Hello
Hello
Hello
Hello
Hello
...
Hello
Hello
Hello
Hello
Hello
...
...
</code>
The <code>Hello</code>s are printed in groups of 5, and the groups are printed in groups of 5.
I have tried this on both Windows and Linux, and the same thing happens. I have also tried using <code>time.sleep()</code> in the <code>run()</code> function, but the same thing happens.
I have also tried using <code>print("Hello", flush=True)</code>, but the same thing happens.
I have also tried using <code>sys.stdout.write("Hello\n")</code>, but the same
