import threading
# Test threading daemon

def natural_numbers():
    n = 0
    while True:
        yield n
        n += 1

def main():
    for i in natural_numbers():
        print(i)
        time.sleep(0.5)
        if i == 5:
            break

t = threading.Thread(target=main)
t.start()
print('Thread started...')

"""
Output:
Thread started...
0
1
2
3
4
5
"""

# Test threading daemon again

def natural_numbers():
    n = 0
    while True:
        yield n
        n += 1

def main():
    for i in natural_numbers():
        print(i)
        time.sleep(0.5)
        if i == 5:
            break

t = threading.Thread(target=main)
t.daemon = True
t.start()
print('Thread started...')

"""
Output:
Thread started...
0
1
2
3
4
5
"""

# Test threading daemon
