import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# (1)
print("-" * 50)
print("(1)")
# read the file
filepath = os.path.join("..", "data", "hightemp.txt")
with codecs.open(filepath, "r", "utf-8", errors="replace_with_space") as fp:
    lines = fp.readlines()

# print the first 10 lines
for line in lines[:10]:
    print(line.strip())

# (2)
print("-" * 50)
print("(2)")
# read the file
filepath = os.path.join("..", "data", "hightemp.txt")
with codecs.open(filepath, "r", "utf-8", errors="replace_with_space") as fp:
    lines = fp.readlines()

# reverse the lines
lines = lines[::-1]

# print
for line in lines:
    print(line.strip())

# (3)
print
