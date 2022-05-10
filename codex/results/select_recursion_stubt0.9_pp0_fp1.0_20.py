import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    r = [F(), F()]
    g = select.select([], r, [], 0)
    for f in r:
        f.close()
</code>
So basically we should catch that in the user code as well. Another example is this one:
<code>&gt;&gt;&gt; class X:
...     pass
... 
&gt;&gt;&gt; class Y:
...     def fileno(self):
...             return X()
... 
&gt;&gt;&gt; class Z:
...     def fileno(self):
...             return Y().fileno()
... 
&gt;&gt;&gt; z = Z()
&gt;&gt;&gt; z.fileno().read
&lt;bound method file.read of &lt;__main__.X instance at 0x7f05c8d15078&gt;&gt;
</code>
Please don't try anything similar in your code at home!

