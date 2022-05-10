from types import FunctionType
list(FunctionType(code,globals())() for code, globals in ((compile(code,"",mode), globals().copy()) for code in (b1,b2)))
</code>
Output
<code>10
20
</code>

