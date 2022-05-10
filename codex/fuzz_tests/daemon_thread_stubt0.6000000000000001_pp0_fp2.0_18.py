import sys, threading

def run():
    while True:
        print(threading.active_count())

threading.Thread(target=run).start()

print('Press enter to exit')
sys.stdin.readline()
</code>
This program prints the number of active threads and waits for user input (which will never come).
On Windows, it prints the following:
<code>2
2
2
2
...
</code>
On Linux, it prints the following:
<code>2
2
2
2
...
2
2
2
2
...
</code>
As you see, the program on Linux occasionally prints the same number twice.
Why does the number of active threads change on Linux?

