import types
types.MethodType(getattr(c, 'dic_to_xml_str'), c)
</code>
The error I get is:
<code>TypeError: descriptor 'dic_to_xml_str' for 'object' objects doesn't apply to a 'type' object
</code>
What am I doing wrong?


A:

First, the method is not a <code>staticmethod</code> so it expects <code>self</code> as the first argument.
Second, the <code>dic_to_xml_str</code> method is a class method, so you need to provide the class as the first argument:
<code>types.MethodType(getattr(c, 'dic_to_xml_str'), c, c)
</code>
Demo:
<code>&gt;&gt;&gt; class c:
...     @classmethod
...     def dic_to_xml_str(cls, dic):
...         return '123'
... 
&gt;&gt;&gt; types.MethodType(getattr(c, 'd
