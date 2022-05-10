from types import FunctionType
list(FunctionType(f.__code__, {}) for f in [lambda: a for a in range(10)])
</code>
Because this actively uses code with which the <code>lambda</code>s are generated, not the <code>lambda</code>s themselves, it can work even before the compiler starts optimizing the code.

