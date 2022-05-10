import select
# Test select.select()

import sys
from select import select
from time import time

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time()
for i in range(5):
    slow_systemcall()
end = time()
print(end - start)

start = time()
for i in range(5):
    select.select([], [], [], 0.1)
end = time()
print(end - start)

print("-" * 50)

start = time()
for i in range(5):
    select([], [], [], 0.1)
end = time()
print(end - start)

start = time()
for i in range(5):
    select.select([], [], [], 0.1)
end = time()
print(end - start)

print("-" * 50)

start = time()
for i in range(5):
    select.select([], [], [], 0.1)
end = time()
