import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
I get an error saying:
<code>ctypes.ArgumentError: argument 3: &lt;class 'TypeError'&gt;: wrong type
</code>
I have tried to change the last argument to a string and the error changes to:
<code>ctypes.ArgumentError: argument 3: &lt;class 'TypeError'&gt;: wrong type
</code>
I have tried to change the last argument to a number, but it says:
<code>ctypes.ArgumentError: argument 3: &lt;class 'TypeError'&gt;: wrong type
</code>
I have also tried to change the last argument to a variable of type int, but it says:
<code>ctypes.ArgumentError: argument 3: &lt;class 'TypeError'&gt;: wrong type
</code>
I have tried to change the last argument to a variable of type long, but it says:
<code>ctypes.ArgumentError: argument 3: &lt;class
