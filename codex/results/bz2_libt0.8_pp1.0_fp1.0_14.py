import bz2
bz2_file = bz2.BZ2File("/Users/amitrajan/Downloads/wiki_00.bz2")
bz2_file.read()[:1000]

#%%
len(bz2_file.read())

#%%
import re
pattern = re.compile("===(.*)===")
match = pattern.search("===A=== heyo ===B===")
match.groups()

#%%
import bz2
bz2_file = bz2.BZ2File("/Users/amitrajan/Downloads/wiki_00.bz2")
pattern = re.compile("===(.*)===")
iterator = (x.group(1) for x in re.finditer(pattern, bz2_file.read().decode()))
len(set(iterator))

#%%
import re
re.match("foo", "foobar")

#%%
re.match("foo", "barfoo")

#%%
re.search("foo", "barfoo")

#%%
re
