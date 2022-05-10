import bz2
bz2.BZ2File(os.path.join(data_dir, 'enwiki-latest-pages-articles.xml.bz2'), 'rb')

# Iterate through the file and print the first 100 lines
with bz2.BZ2File(os.path.join(data_dir, 'enwiki-latest-pages-articles.xml.bz2'), 'rb') as f:
    for i, line in enumerate(f):
        print(line)
        if i == 99:
            break

# Iterate through the file and print the first 100 lines
with bz2.BZ2File(os.path.join(data_dir, 'enwiki-latest-pages-articles.xml.bz2'), 'rb') as f:
    for i, line in enumerate(f):
        print(line)
        if i == 99:
            break

# Iterate through the file and print the first 100 lines
with bz2.BZ2File(os.path.join(data_dir, 'enwiki-latest-pages-articles.xml.bz2
