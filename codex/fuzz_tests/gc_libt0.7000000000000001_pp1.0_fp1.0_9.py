import gc, weakref
class Node:
    pass
n1 = Node()
n2 = Node()
n1.next = n2
n2.prev = n1
n1.ref = weakref.ref(n1)
n2.ref = weakref.ref(n1)
del n1
del n2
gc.collect()
</code>
This is the output from my Mac:
<code>garbage:
[&lt;weakref at 0x1008d6b00; to 'Node' at 0x1008d6940&gt;,
 &lt;weakref at 0x1008d6b08; to 'Node' at 0x1008d6940&gt;,
 &lt;weakref at 0x1008d6ae8; to 'Node' at 0x1008d6940&gt;,
 &lt;weakref at 0x1008d6b10; to 'Node' at 0x1008d6940&gt;,
 &lt;weakref at 0x1008d6b18; to 'Node' at 0x1008d6940&gt
