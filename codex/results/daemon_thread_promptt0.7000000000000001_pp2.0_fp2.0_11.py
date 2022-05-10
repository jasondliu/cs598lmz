import threading
# Test threading daemon
def run_thread(n):
    print('thread', n)

t1 = threading.Thread(target=run_thread, args=(1,))
t1.daemon = True
t1.start()
t1.join(0.01)
print('test')

# Advanced threading daemon
def run_thread1(n):
    print('thread', n)

for i in range(5):
    t = threading.Thread(target=run_thread1, args=(i,))
    if i == 3:
        t.daemon = True
    t.start()
print('done')

# Read data from file
import json
path = r'C:\Users\hanxi\Documents\GitHub\Python-Learn\Practice\ch10\pi_million_digits.txt'
with open(path) as f:
    lines = f.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()

print(pi_string[:50] + '...')
print(len(pi
