from types import FunctionType
list(FunctionType(None,None) for _ in range(1))
from math import sqrt
list(sqrt(x) for x in range(1))
</code>
outputs
<code>[]
[]
</code>
as expected and has the desired effect on my CPU usage

