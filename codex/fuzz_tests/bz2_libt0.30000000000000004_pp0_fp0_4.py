import bz2
bz2_file = bz2.BZ2File('/Users/jason.katz/Downloads/enwiki-latest-pages-articles.xml.bz2')

# this is a generator that yields one line at a time
# we'll use it to read the data in chunks
def get_next_line(file_object):
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data

# this is a generator that yields lists of lines
# we'll use it to read the data in chunks
def get_next_chunk(file_object, chunk_size=10000):
    lines = []
    for line in get_next_line(file_object):
        lines.append(line)
        if len(lines) == chunk_size:
            yield lines
            lines = []
    yield lines

# this is a generator that yields chunks of xml
# we'll use it to read the data in chunks
def get_next_xml_chunk(file_object, chunk_size=10000):
    lines = []
    for
