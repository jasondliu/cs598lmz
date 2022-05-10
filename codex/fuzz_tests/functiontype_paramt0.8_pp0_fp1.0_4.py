from types import FunctionType
list(FunctionType(_)for _ in vars(math))

"""
A better way is to use inspect.getmembers()
to extract all of the names that are functions:
"""

import math
import inspect
[name for name, obj in inspect.getmembers(math) if inspect.isfunction(obj)]

"""
Extracting parts of a datetime and putting them back together is a common operation.
For example, you might want to keep the year and month but replace the day with a constant.
"""

from datetime import datetime
d = datetime(2012, 12, 21)
d.replace(minute=0, hour=0, second=0)

"""
Given a list of filenames, you want to rename them 
to include a timestamp indicating when they were last modified.
"""

import os
from datetime import datetime

files = ['src/data/file1.txt','src/data/file2.txt','src/data/file3.txt']

for f in files:
    os.utime(f, times=(datetime.now().timestamp(), datetime.now().
