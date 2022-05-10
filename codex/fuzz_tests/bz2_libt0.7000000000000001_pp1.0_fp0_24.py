import bz2
bz2.decompress(line)

#%%
#bz2file=bz2.open(r'C:\Users\Administrator\Downloads\mwcomments\AA\wiki_00')
#bz2file.readline()

#%%
'''
f=open(r'C:\Users\Administrator\Downloads\mwcomments\AA\wiki_00','rb')
for line in f:
    print(line)
    break
f.close()
'''

#%%
import bz2
f=bz2.open(r'C:\Users\Administrator\Downloads\mwcomments\AA\wiki_00','rb')
for line in f:
    print(line)
    break
f.close()

#%%
import bz2
f=bz2.open(r'C:\Users\Administrator\Downloads\mwcomments\AA\wiki_00','rb')
print(f.readline())
f.close()

#%%
# using bz2file
bz2file=bz2.open(
