import types
types.new_class( "X", (object,) )
# Script is crashing at following line becasue type is not ready yet
# types.new_class( "X", (object,) )
</code>
So I am getting following error:
<code>&lt;type 'exceptions.TypeError'&gt;: attribute name must be string, not 'type'
     args = ("attribute name must be string, not 'type'",)
     message = 'attribute name must be string, not 'type''
</code>
I have tried on python 2.4, 2.5 and 2.6 on linux.
Thanks in advance for any reply. 


A:

You need to use the <code>__dict__</code> attribute of the new class. Here's one way that works OK:
<code>import types

types.new_class("X", (object,), {
    "__dict__": {
        "somethong": "Something"
    }
})
</code>

<code>&gt;&gt;&gt; x = X()
&gt;&gt
