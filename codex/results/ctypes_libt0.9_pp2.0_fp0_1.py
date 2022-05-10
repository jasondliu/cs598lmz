import ctypes
ctypes.windll.ole32.CoInitialize(0)
</code>
It worked well in other modules, but here it said:
<code>AttributeError: module 'ctypes' has no attribute 'windll'
</code>
I tried <code>ctypes.cdll.cOle32.CoInitialize(0)</code>, but it also said:
<code>AttributeError: function 'CoInitialize' not found
</code>
Since I am programming on a Pi, I had to find another way. After searching, I made a <code>if platform.system() == 'Windows'</code> trigger, but I can't find any way to use it on Windows.
And I need all the information that is able to jump the browser to load so I can use it to do other things.
Can anyone tell me a possible solution? I am working in PyCharm on Raspbian, and I would also like to deploy it to Windows.

