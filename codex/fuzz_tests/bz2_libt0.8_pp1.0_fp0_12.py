import bz2
bz2.decompress(image_data)

import tarfile
tar = tarfile.open("data/sample.tar.gz", "r:gz")
tar.extractall(path='data/')
tar.getmembers()

# Regular Expression
import re
pattern = r"spam"
if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No match")

match = re.search(pattern, "eggspamsausagespam")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)

# File System
import os
for root, dirs, files in os.walk("data/"):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root,file
