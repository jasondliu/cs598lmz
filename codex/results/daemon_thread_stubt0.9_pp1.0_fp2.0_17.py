import sys, threading

def run():
    print("I am working yet")
    time.sleep(0.5)

while True:
    t = threading.Thread(target=run)
    t.start()
</code>
It gives
<code>I am working yet
I am working yet
I am working yet
I am working yet
</code>
you may consider to put your code in a function and then use it in the threading. So that, the changes inside the function do not affect the global variable.

