from types import FunctionType
list(FunctionType(x,globals()).__globals__.keys())[0:5]

# %%
import numpy as np
a=np.array([[1,2],[3,4]])
np.sum(a,axis=0)

# %%
import numpy as np
a=np.random.randn(2,2)
a

# %%
import numpy as np
a=np.random.randn(2,2)
b=np.random.randn(2,2)
np.multiply(a,b)

# %%
import numpy as np
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = a[0:2, 1:3]
b[0,0]=77
print(a)

# %%
import numpy as np
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
row_r1 =
