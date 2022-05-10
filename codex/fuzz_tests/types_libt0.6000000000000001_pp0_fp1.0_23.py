import types
types.new_class( "Widget",
                 bases = (object,),
                 kwds  = {'children':[]} )

x = Widget()
x.children.append( Widget() )

print(x.children[0])
</code>
which prints out:
<code>&lt;Widget object at 0x7f9e9e2d6950&gt;
</code>

