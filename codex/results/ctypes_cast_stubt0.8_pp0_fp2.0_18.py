import ctypes
ctypes.cast(0, ctypes.py_object).value

filename = 'my_vector.txt'

with open(filename) as f:
    vector = []
    for line in f:
        vector.append(int(line.strip()))

print(str(vector))
</code>


A:

First, you can read all lines at once with <code>readlines()</code> instead of looping over the file object:
<code>with open(filename) as f:
    vector = f.readlines()

vector = [int(x.strip()) for x in vector]
</code>
Second, if you want to strip only the trailing newline, use <code>rstrip()</code>:
<code>with open(filename) as f:
    vector = f.readlines()

vector = [int(x.rstrip('\n')) for x in vector]
</code>

