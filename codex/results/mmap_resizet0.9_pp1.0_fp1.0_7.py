import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expected <code>a</code> to be empty but instead its value is <code>b'\x01'</code>.


A:

Just for completeness sake. I've tested it on the <code>venv</code> set up like this:
<code>(venv) $ python --version
Python 3.6.5
(venv) $
</code>
Here is mine <code>test</code> file:
<code>(venv) $ ls -l test
-rw-r--r--. 1 devtools devtools 50 Dec  8 18:56 test
(venv) $ head -c 1 test
1
(venv) $
</code>
And the code:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
And the output:
<code>(venv) $ python test.py 
b'\x
