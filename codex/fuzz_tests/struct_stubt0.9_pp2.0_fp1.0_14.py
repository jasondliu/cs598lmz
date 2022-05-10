from _struct import Struct
s = Struct.__new__(Struct)
i = int(100000000000000000000000000000000000000000)
n = i.__neg__()
</code>
In my example, I print the Struct class pointer for the two 'struct' instances I constructed. One of them is the same, but the other is not. This is a problem as I want code similar to:
<code>from _struct import Struct
class MyStruct(Struct):
  def mymethod(self):
    print('mymethod')

s = MyStruct.__new__(MyStruct)
</code>
And in this example, when I call <code>s.__sizeof__()</code> from Python, I want to call <code>s.__sizeof__()</code> from C. To do this I would need two 'structs' that have a different <code>self-&gt;ob_type</code>, even if they have the same <code>self-&gt;ob_type-&gt;tp_base</code>
In other words, I need <code>self-&gt;ob_type-&gt;tp_base != self-&gt;ob_type</code
