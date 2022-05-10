import lzma
lzma.open

fp = 'filename.tar'

print("opening")
tar = tarfile.open(fp, "r")

print("extracting")
tar.extractall()

print("closing")
tar.close()
</code>
But I get this error:
<code>opening
Traceback (most recent call last):
  File "C:/Users/Jack/PycharmProjects/untitled1/tar.py", line 7, in &lt;module&gt;
    tar = tarfile.open(fp, "r")
  File "C:\Users\Jack\AppData\Local\Programs\Python\Python37-32\lib\tarfile.py", line 1634, in open
    t = cls.taropen(name, mode, fileobj, **kwargs)
  File "C:\Users\Jack\AppData\Local\Programs\Python\Python37-32\lib\tarfile.py", line 1572, in taropen
    return func(name, mode, fileobj, **kwargs)
TypeError: required argument is not an integer
