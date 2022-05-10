import ctypes
ctypes.cast(p, ctypes.py_object).value

#%%
# for each file in location
#   -- get text from pdf
#   -- write text to txt file
#%%

import os

#%%
#print(os.listdir(location))
#%%
#for filename in os.listdir(location):
#    print(filename)
#%%
#for i, filename in enumerate(os.listdir(location)):
#    print(i, filename)
#    if i == 5:
#        break
#%%
#for i, filename in enumerate(os.listdir(location)):
#    if filename.endswith('.pdf'):
#        print(i, filename)
#%%
#for i, filename in enumerate(os.listdir(location)):
#    if filename.endswith('.pdf'):
#        print(i, filename)
#        filename_txt = filename[:-4] + '.txt'
#        print(filename_txt)
#%%
#for i, filename in enumerate(os.listdir
