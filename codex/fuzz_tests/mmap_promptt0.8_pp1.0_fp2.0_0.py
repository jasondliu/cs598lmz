import mmap
# Test mmap.mmap

f = open('/Users/leo/Downloads/150-0.txt', 'r+b')
m = mmap.mmap(f.fileno(), 0)


print('Original content:', m.readline().rstrip())  # prints "Hello Python!"

m.seek(0)
m.write(b'Hello World!')
m.seek(0)
print('Modified content:', m.readline().rstrip())  # prints "Hello World!"

m.close()
</code>
The result is:
<code>Original content: b'Hello Python!'
Modified content: b'Hello World!'
</code>
However, when I tried to use it in a Django project, I got the error below:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/Users/leo/.venvs/test/lib/python3.5/site-packages/django/test/testcases.py", line 697, in __call__
