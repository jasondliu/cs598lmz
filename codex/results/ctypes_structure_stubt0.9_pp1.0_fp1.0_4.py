import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 2
print S()
</code>
prints <code>&lt;__main__.S instance at 0x2&gt;</code> indicating a non-empty instance. 
But if I change the last line to <code>print S().x</code>, I get an empty string. 
What am I don't understand about this code? The output of <code>S()</code> seems to indicate that there are two characters in <code>S().x</code>, but printing <code>S().x</code> doesn't print those two characters. 
UPDATE:
On the advice of Ian in the comments, I have tried:
<code>print '|', S().x, '|'
</code>
and this gives the output <code>||</code>. 
So, there is some stuff inside the buffer <code>S().x</code>, but it is not printing. 
UPDATE:
It appears that the empty string behavior is platform-dependent. Further updates will appear in comments, below. 


A:

Actually that is not surprising. Its not an errant string. You
