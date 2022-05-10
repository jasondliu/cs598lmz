import codecs
codecs.open('test.txt', encoding='utf_8')

# Importing with a specific name
import numpy as np
np.array([1, 2, 3])

# Importing a specific function
from datetime import date
date(2018, 1, 1)

# Importing a specific function directly into the namespace
from datetime import date
date(2018, 1, 1)

# Importing multiple functions at once
from datetime import date, timedelta
date(2018, 1, 1)
timedelta(days=1)

# Importing all functions in a module (generally discouraged)
from datetime import *
date(2018, 1, 1)
timedelta(days=1)

# Importing a module into a namespace (generally discouraged)
import datetime as dt
dt.date(2018, 1, 1)
dt.timedelta(days=1)

# Exploring modules with dir()
import numpy as np
x = np.array([1, 2, 3])
dir(x)

# Exploring modules with dir()
import numpy as
