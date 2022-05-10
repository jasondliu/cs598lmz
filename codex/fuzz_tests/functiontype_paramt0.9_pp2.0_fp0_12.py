from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, 'name', None, None))
globals().keys()
dir()
dir(function)
import pandas as pd
from io import StringIO
import numpy as np
data = '''
1,2,3
4,5,6
'''
pd.read_csv(StringIO(data))
pd.read_csv(StringIO(data), skiprows=1)
data = '''
age,city,zip_code1
20,    'toronto',  2223
32,    'caracas',  3223
'''
pd.read_csv(StringIO(data), skipinitialspace=True)
pd.read_csv(StringIO(data), skipinitialspace=False)
pd.read_csv(StringIO(data), skipinitialspace=True)
data = '''
age                 ,city,zip_code1
20,    'toronto',  2223
32,    'caracas',  3223
'''
pd.read_csv(StringIO(data), usecols=['age
