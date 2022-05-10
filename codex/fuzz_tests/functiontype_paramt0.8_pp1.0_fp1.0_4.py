from types import FunctionType
list(FunctionType(filter, [], {}).__globals__.keys())

#%%
import pandas as pd
import math

def common_function(value):
    if not math.isnan(value):
        return math.log10(value)
    else:
        return value
        
df = pd.DataFrame(
    {
        "A": [1, 2, 3, 4, 5, 6, 7],
        "B": [2, 4, 6, 8, 10, 12, 14],
        "C": [None, None, None, 10, 30, 100, 500]})
        
df['A_logged'] = df['A'].apply(common_function)
df['B_logged'] = df['B'].apply(common_function)
df['C_logged'] = df['C'].apply(common_function)

print(df)

#%%
# use lambda instead
import pandas as pd
import math

df = pd.DataFrame(
    {
        "A": [1, 2, 3, 4,
