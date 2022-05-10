import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
This works but the text is not displayed properly. The letters are not displayed in the right order.
This is how it looks like:

I had a similar problem in C++, but I solved it by specifying the encoding.
Any ideas?


A:

It seems that <code>MessageBoxW</code> expects a unicode string. So I had to use <code>u"your text"</code> instead of <code>"your text"</code>.

