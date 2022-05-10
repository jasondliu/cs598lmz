import types
types.MethodType(foo, 0)
</code>
But this is a prime source of side effects.
In solidity, it is not like that. You can not alter a function.
But you can implement a function <code>foo(uint a)</code>. If you do so, then in fact you are implementing a function <code>foo(uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint,uint)</code>. And <code>foo(1)</code> is in fact <code>foo(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)</code>. The arguments are padded with zeroes.
How can you be sure that the first argument is a 0, and not a 1 for instance ?
