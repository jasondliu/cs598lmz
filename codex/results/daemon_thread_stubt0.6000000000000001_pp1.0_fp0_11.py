import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(2)

t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

while True:
    print("Goodbye")
    time.sleep(2)
</code>
Output:
<code>Goodbye
Hello
Hello
Hello
Hello
...
</code>

