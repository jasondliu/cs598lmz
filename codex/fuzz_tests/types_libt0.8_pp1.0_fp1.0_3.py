import types
types.ClassType
</code>
Which I had previously misinterpreted as the class <code>ClassType</code>. Now I know better, I see it is returning the type <code>type</code>. Is there a way, within Python, to get the class <code>ClassType</code>?
(For those that may be interested, I'm trying to achieve something like this).
EDIT:
I've found the easiest way to achieve what I was after is to simply use <code>types.ClassType.__name__</code> instead of the class <code>ClassType</code>. I'm still curious though, if there is a way to get the class <code>ClassType</code> from within Python.


A:

The <code>types.ClassType</code> is a function that created a new class object:
<code>&gt;&gt;&gt; types.ClassType
&lt;type 'type'&gt;
&gt;&gt;&gt; class_obj = types.ClassType('Foo', (), {})
&gt;&gt;&gt; class_obj
&lt;class 'F
