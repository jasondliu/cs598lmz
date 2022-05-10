import sys, threading
threading.Thread(target=lambda: sys.stdin.read()).start()

#

import threading
t = threading.Thread(target=some_function_i_want_to_run)
t.setDaemon(True)
t.start()

#

foo = lambda x: x+1
print foo(1)

foo = (lambda x, y, z: x + y + z)(1,2,3)
print foo

#

f = open('names_and_ages.csv')

def line_to_dict():
    dicts = []
    for line in f:
        name, age = line.split(',')
        dicts.append({'name': name.strip(), 'age': int(age.strip())})
    return dicts

print line_to_dict()

f = open('names_and_ages.csv')
def line_to_dict():
    for line in f:
        name, age = line.split(',')
        yield {'name': name.strip(), 'age': int(age.strip())}

print list
