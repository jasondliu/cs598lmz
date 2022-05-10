from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(sb_compressed)

#bz2 is really really slow

from zlib import decompress
decompress(sb_compressed)

#zlib is much faster

# ## dbm

# Now let's look at the dbm module.  

# + {"code_folding": [0]}
import dbm

# + {"code_folding": [0]}
# Let's start with a dictionary
my_dict = {"Sterling Archer": "Handsome Secret Agent",
           "Bob Belcher": "Hamburger Restaurant Owner",
           "Ben Wyatt": "Accountant, Former Mayor"}

# + {"code_folding": [0]}
# Let's save it to a database
db = dbm.open('savedatabase', 'c')
db.update(my_dict)
db.close()

# + {"code_folding": [0]}
# Now let's read it back in
db = dbm.open('savedatabase')
db.keys()
# -

# ## shelve

# The shelve
