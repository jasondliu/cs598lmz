import bz2
bz2.BZ2File()
get_ipython().run_line_magic('pwd', '')
filename = 'Land_Cover_types.txt'
path = '/Users/kimberlycaviness/Documents/EcoDataScience'
f = open(filename)
print(f)
f = open(filename, "r")
f.read()
f.read()
f.read()
help(f.seek)
f.readlines()
f.seek()
f.seek(0)
f.readlines()
f.close()
lines = f.readlines()
lines
lines[0]
with open(filename) as f:
    lines = f.readlines()
lines[0]
lines[1]
lines[-1]
lines[-2]
f = open(filename, "r")
lines
f.close()
lines[0].lstrip("b").strip("'")
lines[0].lstrip("b'").strip("'")
f = open(filename)
lines = [line.lstrip("b'").strip("'\n")
