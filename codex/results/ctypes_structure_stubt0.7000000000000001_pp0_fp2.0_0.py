import ctypes

class S(ctypes.Structure):
    x = 1.0
    y = 1.0

ctypes.windll.user32.MessageBoxW(0, "test %f %f" % (S.x, S.y), "title", 0)
</code>
This brings up a message box with the values <code>0.0</code> and <code>0.0</code>. How do I get the message box to show <code>1.0</code>?


A:

You need to create an instance of the structure first.
<code>class S(ctypes.Structure):
    x = 1.0
    y = 1.0

s = S()
ctypes.windll.user32.MessageBoxW(0, "test %f %f" % (s.x, s.y), "title", 0)
</code>

