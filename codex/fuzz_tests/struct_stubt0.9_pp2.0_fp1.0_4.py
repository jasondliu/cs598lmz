from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('format', 'NNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNldaNNLdaNNL')
n = 0
for c in s.format:
   n = n + 1
   print c
</code>


A:

As can be seen from the <code>repr()</code> of <code>struct</code> format string <code>s.format</code>, <code>self._fmt</code> is actually an instance of <code>_clearcache</code>. The <code>_clearcache</code> class is not defined in the <code>
