import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
import numpy as np
np.array(x, copy=False)

#%%
import numpy as np
np.array(x, copy=False, subok=True)

#%%
import numpy as np
np.asarray(x)

#%%
import numpy as np
np.asanyarray(x)

#%%
import numpy as np
np.ascontiguousarray(x)

#%%
import numpy as np
np.asfortranarray(x)

#%%
import numpy as np
np.asarray_chkfinite(x)

#%%
import numpy as np
np.asscalar(x)

#%%
import numpy as np
np.require(x, dtype=None, requirements=None)

#%%
import numpy as np
np.copy(x)

#%%
import numpy as np
np.copyto(dst, src, casting='same_kind', where=True)

#
