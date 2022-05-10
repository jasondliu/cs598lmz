import ctypes
ctypes.windll.user32.MessageBoxW(0, "Hello world!", "Hello", 1)
</code>
On my system (Win7), this produces a nice, simple message box that says:
<blockquote>
<p>Hello world!</p>
</blockquote>
and has one button, labelled "Hello".
The problem is that the button doesn't do anything.  If I click it, the message box disappears, but nothing happens.
The documentation for MessageBoxW says:
<blockquote>
<p>The return value specifies the
  user's action.</p>
</blockquote>
but I don't know how to get this return value.
What should I do?


A:

You're looking for MessageBoxExW. This function also takes a pointer to a variable that receives the return value.
In your case it would look something like this:
<code>import ctypes
result = ctypes.c_uint()
ctypes.windll.user32.MessageBoxExW(0, "Hello world!", "Hello", 1, 0, result)
print(result.value)
</code>
