from bz2 import BZ2Decompressor
BZ2Decompressor

# %% [markdown]
# The syntax to import a function from a library can be confusing. We'll look at
# more examples later.

# %% [markdown]
# ## Importing packages

# %% [markdown]
# We have used some elements of NumPy, Pandas and PyTorch already. In order that
# we can use them we have had to import them, by saying:

# %%
import numpy as np
import pandas as pd
import torch

# %% [markdown]
# The command "import numpy as np" imports everything in the NumPy library, and
# then instead of having to write numpy.array or numpy.abs etc, we can just write
# np.array or np.abs.
#
# To see the functions and types we can use in NumPy, do

# %%
help(np)

# %% [markdown]
# and so on for the other libraries.
#
# However, this doesn't actually import everything from the library. If a
# function has been optimised, it might not be loaded. Some of the more advanced
