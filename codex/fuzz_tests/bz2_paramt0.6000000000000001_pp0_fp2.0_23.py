from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# data is a byte array
# this is how we convert it to a string
s = data.decode("utf-8")
s

# split the string into lines
lines = s.split("\n")
lines

# each line is a JSON object
import json
json.loads(lines[0])

# some of the lines are empty
[json.loads(line) for line in lines if len(line) > 0]

# let's see what we have
lines[:10]

# let's see what we have
lines[-10:]

# let's see what we have
lines[0]

# let's see what we have
lines[1]

# let's see what we have
lines[-1]

# let's see what we have
lines[-2]

# let's see what we have
lines[-3]

# let's see what we have
lines[-4]

# let's see what we have
lines[-5]

# let's see what we have
lines[-
