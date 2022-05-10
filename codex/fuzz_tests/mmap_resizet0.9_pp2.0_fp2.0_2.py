import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # should raise a ValueError
</code>
But the exception doesn't seem to be raised ("End"))
<code>C:\Python27\python.exe "D:/Python/PyCharm Projects/test/new/test.py"
End

Process finished with exit code 0
</code>
I use Python 2.7 x86 on Windows. Does anybody know how raise the exception and prevent the code from continuing?
I read that: 
<blockquote>
<p>In general, ValueError is raised when a built-in operation or function
  receives an argument that has the right type but an inappropriate
  value</p>
</blockquote>
So I guess there should be no difference in the output of
<code>a = m[:]  # should raise a ValueError if it is raised
</code>
and
<code>a = m[:2] #should raise a ValueError if it is raised
</code>
Is it right?


A:

<blockquote>
<p>Does anybody know how raise the exception and prevent the code from continuing?</p>
</blockquote>
It's
