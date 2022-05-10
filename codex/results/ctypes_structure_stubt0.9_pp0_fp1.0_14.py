import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float()
    y = ctypes.c_int()

s = S()
print 'before setting: ',
print s.x, s.y

s.x = 1.2
s.y = 12
print 'after setting: ',
print s.x, s.y
</code>
And I get:
<code>('before setting: ', 1.2, 12)
('after setting: ', 1.2, 12)
</code>
Note that it may not be easy to find the correct syntax to do what you're trying in python. But you can always cast your void ** to a void ** to a void ** to a void ** to a void ** to a S ** using type() first.

