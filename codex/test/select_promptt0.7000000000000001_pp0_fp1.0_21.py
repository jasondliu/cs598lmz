import select
# Test select.select with stdin
import os

r, w, x = select.select([0], [], [], 0.1)
print("stdin in r:", 0 in r)
print("stdin in w:", 0 in w)
print("stdin in x:", 0 in x)
print("stdin in r:", os.fdopen(0) in r)
print("stdin in w:", os.fdopen(0) in w)
print("stdin in x:", os.fdopen(0) in x)

# Test select.select with a file
f = open("/etc/passwd")
r, w, x = select.select([f], [], [], 0.1)
print("file in r:", f in r)
print("file in w:", f in w)
print("file in x:", f in x)
