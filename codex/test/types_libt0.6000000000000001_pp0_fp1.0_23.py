import types
types.new_class( "Widget",
                 bases = (object,),
                 kwds  = {'children':[]} )

x = Widget()
x.children.append( Widget() )

print(x.children[0])
