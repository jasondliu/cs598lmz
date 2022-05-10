import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()
# print('Hello from main thread')

import time
start = time.time()
time.sleep(0.23)
end = time.time()
print(end - start)

import zen
seed = zen.random.seed(2)
zen.random.randint(-1, 1)
zen.random.random()
zen.random.shuffle(range(2))

sandbox = zen.Sandbox()
print(sandbox.globals())
sandbox.globals_update({'dictionary': {'a': 2, 'b': 3}, 'list': [1, 2], 'value': 1})

print(sandbox.eval('bool(dictionary)', True))
print(sandbox.eval('1 + len(dictionary) + value', True))
print(sandbox.code_call('''
if len(dictionary) > 1:
    x = dictionary['a'] + dictionary['b']
else:
    x = 0''', {'dictionary': {
