import ctypes

class S(ctypes.Structure):
    x = 1

print S.x
</code>
This seems to be pretty straightforward.  <code>S.x</code> is defined to be the integer <code>1</code> so the output should be <code>1</code>. But that's not the case.
<code>&gt;&gt;&gt; python struct_test.py 
&lt;field 'x' of 'S' structures&gt;
</code>
What's happening here? I'm using python 2.5.5.


A:

Found the answer. I should have done
<code>print S.x.value
</code>
because the value is stored in a field <code>value</code> of type <code>c_int</code>.

