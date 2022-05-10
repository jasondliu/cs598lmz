import codecs
codecs.encode(file_name, "rot_13")

print(file_name)
</code>
The file_name is:
<code>G:/Eclipse/workspace/PythonProject/Python/src/Python/Xé-Lé-Né_09.jpg
</code>
And the error message is:
<code>Traceback (most recent call last):
  File "C:/Users/academy.python/Desktop/Python/Python_Functions.py", line 155, in &lt;module&gt;
    codecs.encode(file_name, "rot_13")
  File "C:\Users\academy.python\AppData\Local\Programs\Python\Python36-32\lib\codecs.py", line 690, in encode
    raise TypeError("'encoding' must be a string")
TypeError: 'encoding' must be a string
</code>


A:

You forgot to assign the result:
<code>file_name = codecs.encode(file_name, "rot_13")
</code>
