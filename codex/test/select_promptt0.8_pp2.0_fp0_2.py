import select
# Test select.select(rlist, wlist, xlist[, timeout])
rlist = []
wlist = [1, 3, 5]
xlist = [2, 4, 6]

select.select(rlist, wlist, xlist, 1)

# Uncomment to see  the results in your IDE
# print(rlist)
# print(wlist)
# print(xlist)
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# 12.
# Import numpy package and generate a random 10X2 numpy array
import numpy as np
# Generating a random array of 10 X 2
np.random.rand(10, 2)

# Uncomment to see  the results in your IDE
# print(np.random.rand(10,2))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# 13.
# Import numpy package and create an array of 10 evenly spaced numbers between 0 and 1
import numpy as np
# Generating a random array of 10 X 2
np.linspace(0, 1, 10, endpoint=True)
