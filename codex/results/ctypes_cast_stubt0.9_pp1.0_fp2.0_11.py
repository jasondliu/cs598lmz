import ctypes
ctypes.cast(l, ctypes.py_object).value = l[-1::-1]
print(l)

&gt;&gt;&gt; (1, 2, 3, 4)
</code>
You don't need it to be an int, though. You could just do this:
<code>&gt;&gt;&gt; l = [1, 2, 3, 4]

&gt;&gt;&gt; print([l[-1]] + l[:-1])
&gt;&gt;&gt; [4, 1, 2, 3]
</code>
If you do want it to be an int, you could also convert it to a string and then recast as a numeric type:
<code>&gt;&gt;&gt; l = [(1, 1, "1"), (2, 1, "2"), (3, 1, "3"), (4, 1, "4")]

&gt;&gt;&gt; [i[-2::]+i[:2]]+l[:-1]
&gt;&gt;&gt; [(2
