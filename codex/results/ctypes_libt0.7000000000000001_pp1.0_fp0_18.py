import ctypes
ctypes.windll.shell32.IsUserAnAdmin()
</code>
This comes up with a "True" result.
Any help would be much appreciated!


A:

I've experienced similar issues when I was working with the pywin32 library. For example, the win32com.client.Dispatch call would simply hang the function and never return. What I did was to put the win32com.client.Dispatch call in a separate thread. After that everything worked as expected.

