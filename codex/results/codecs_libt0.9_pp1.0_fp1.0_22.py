import codecs
codecs.encode()

#%%
import os
os.getcwd()
os.listdir()

#%%
for f in os.listdir():
    print(os.path.join(os.getcwd(), f))

#%%
import os
import sys

print(sys.argv)

#%%
import os
import sys

print(len(sys.argv))

#%%
import os
import sys

def cli_print(*args):
    print(*args)
    
if len(sys.argv) != 2:
    cli_print("Missing argument")
    sys.exit(-1)
else:
    cli_print("Success!")
    
#%%
import os

os.remove("filename")
#%%
import os

for f in os.listdir("/home/jooyeong/Desktop"):
    if os.path.isfile(f):
        os.remove(f)

#%%
import os

for f in os.listdir("/home/jooyeong/Desktop
