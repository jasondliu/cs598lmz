from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(5))
</code>
<blockquote>
<p>File "", line 1
      list(FunctionType(lambda x: x, globals()) for x in range(5))
                                                            ^
  SyntaxError: Generator expression must be parenthesized if not sole argument</p>
</blockquote>
Why does this happen?

