import mmap, os

with open('data/coordinates.csv', 'rb', 0) as f:
    # memory-map the file, size 0 means whole file
    map = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    line = map.readline()  # read the first line
    while line:
        # Remove newline char
        line = line.rstrip()
        print(line)
        line = map.readline()
</code>
This is how it does looks in code. However, I still don't get it how it works. Does this process allows to interprete from every line from the document, then leave memory and so on...?

