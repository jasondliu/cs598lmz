import mmap
# Test mmap.mmap a text file and perform a regular expression match while iterating.
with mmap.mmap(open('file.txt', 'r').fileno(), 0,
               access=mmap.ACCESS_READ) as m:
    for line in iter(m.readline, ""):
        if re.match(r'^\s*#', line):
            print(line.rstrip())
