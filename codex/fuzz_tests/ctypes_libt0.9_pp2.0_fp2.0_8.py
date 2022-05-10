import ctypes
ctypes.windll.kernel32.SetConsoleTextAttribute(std_output_hdl, color)
</code>
but I would strongly recommend to not do this. It is considered bad practice to depend on the environment in programming.
Instead I would recommend to just print the text, and then separately add the information. So something like
<code>print("My Text and more", color)
</code>
is better than
<code>print("My Text and more", end="")
print(".", color)
print(".", color)
...
</code>

