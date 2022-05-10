from types import FunctionType
list(FunctionType(2, 3, {}).__code__.co_freevars)

# => ('a', 'b')

# However, note that, as a function closes over a variable, the variable retains as strong as a reference to the function as the function retains to the variable, so both the variable and the function will be retained in memory forever (until no longer required), even if the function object is otherwise not reachable. This can lead to unwanted memory bloat. For example:

for x in range(100000):
    def x(a, b): return a + b

# Thus, it is recommended to avoid using closures where possible. If you find yourself using a closure and you find that you mutate it, then most likely closure is not what you're after and should try to use class-based object oriented programming instead.


# Further reading
# More information can be found in the following documentations:
# PEP 227: Statically Nested Scopes
# PEP 3104: Access to Names in Outer Scopes
# PEP 3107: Function Annotations
# PEP 3135: Extended Iterable Unpacking
# PEP 3136: Extended Call Synt
