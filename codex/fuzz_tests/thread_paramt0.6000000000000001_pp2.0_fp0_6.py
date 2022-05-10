import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()

# %load lambdas_and_list_comprehensions.py
#!/usr/bin/env python
# encoding: utf-8

# Lambdas and list comprehensions

print("map(lambda x: x**2, range(10)):", map(lambda x: x**2, range(10)))
print("[x**2 for x in range(10)]:", [x**2 for x in range(10)])

print("map(lambda x: x**2, range(10)):", map(lambda x: x**2, range(10)))
print("[x**2 for x in range(10)]:", [x**2 for x in range(10)])

print("[x**2 for x in range(10) if x%2 == 0]:", [x**2 for x in range(10) if x%2 == 0])

# %load generators.py
#!/usr/bin/env python
# encoding: utf-8

# Generators

def my
