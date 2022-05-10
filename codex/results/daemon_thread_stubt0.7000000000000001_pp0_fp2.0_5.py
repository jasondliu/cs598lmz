import sys, threading

def run():
    print("yo")
    time.sleep(10)
    print("wazzup")

threading.Thread(target=run).start()

while True:
    print("hello")
</code>
This will print:
<code>hello
yo
hello
hello
...
hello
hello
wazzup
hello
hello
...
</code>

