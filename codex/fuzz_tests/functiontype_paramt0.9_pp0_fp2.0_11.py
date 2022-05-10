from types import FunctionType
list(FunctionType(add.__code__, globals(), "add", add.__defaults__, add.__closure__)
        .__closure__)
# tuple, length 1
# function object at 0x2641f90, with type 'function' at 0x2641e60
# value 2
</code>
This function is a copy of the original, with different globals and closure.
The problem with this is:
<code>def add(a, b):
  def add3():
    return a + b + c
  c = 3
  return add3()

list(FunctionType(add.__code__, globals(), "add", add.__defaults__, add.__closure__)
        .__closure__)
# tuple, length 1
# function object at 0x2641050, with type 'function' at 0x2641e60
# value 3  # &lt;&lt;-- incorrect value
</code>
The function's closure is correct, but the value of the cell is wrong. Since the function was defined inside a function, the cell's value was determined after definition. Normally a function
