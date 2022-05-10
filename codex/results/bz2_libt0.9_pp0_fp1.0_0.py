import bz2
bz2.compress(b"hello world")
</code>
The output:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: must be bytes or buffer, not str
</code>
Now I tried to change the interpreter in PyCharm: I went to <code>Project Interpreter</code> and <code>Edit</code> the default interpreter to be <code>/usr/bin/python3.6</code>
This didn't work as well as it is still showing the same error.
So the question: For what is <code>/usr/bin/python3.5</code> used? And how do I change the PyCharm interpreter?


A:

Interpreters are not scripts but independent processes. You have to  add them to the list of interpreters manually and choose the correct one when you create a new project.

