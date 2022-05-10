import sys, threading

def run():
    print("Thread started")
    for i in range(10):
        print(i)
        time.sleep(1)
    print("Thread ended")

print("Main started")
t = threading.Thread(target=run)
t.start()
print("Main ended")
</code>
Output:
<code>Main started
Thread started
Main ended
0
1
2
3
4
5
6
7
8
9
Thread ended
</code>

