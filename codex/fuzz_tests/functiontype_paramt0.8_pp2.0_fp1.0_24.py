from types import FunctionType
list(FunctionType('firstParam', globals(), [], ('',), (2, 3))
for i in 2, 3)
</code>
I know that the error lies in the for-loop, but what precisely about the for-loop is wrong (python 3.4 does not help with the error message here) and how can I fix it?


A:

You need to add a colon to your loop.
<code>from types import FunctionType
list(FunctionType('firstParam', globals(), [], ('',), (2, 3))
for i in (2, 3))
</code>
As others have mentioned, the way you've written it, the parser expects you to be assigning the value of <code>FunctionType('firstParam', globals(), [], ('',), (2, 3))</code> to <code>i</code>, but you're calling it in the place where an assignment would go.

