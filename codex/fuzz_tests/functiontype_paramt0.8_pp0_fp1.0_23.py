from types import FunctionType
list(FunctionType("a,b,c",{'a':2},("b","c"),"return b+c",("b","c"),("return b+c",),("return b+c",))\
         .__code__.co_freevars)
</code>
Can you tell me where these strange tuple comes from? I've been searching in the documentation, but I haven't found anything that is able to explain this behaviour.


A:

There are several ways of creating function objects.  <code>FunctionType</code> is one of them.
The constructor expected parameters are documented as:
<blockquote>
<p>types.FunctionType(code, globals[, name[, argdefs[, closure]]])</p>
</blockquote>
In your example, you are only providing <code>code</code> and <code>globals</code> and using default values for the rest of the parameters.
The code is provided as a raw string, so you are really using:
<code>FunctionType(
    compile("a,b,c", "&lt;string&gt;", "exec"),
   
