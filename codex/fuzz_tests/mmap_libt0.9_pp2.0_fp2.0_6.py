import mmap
import re
import io

h = gzip.open('small.osm.pbf','rb')
s = h.read(100000000)

r = pbf.parse_proto_file(gzip.open('small.osm.pbf', 'rb'))
info = iter(r).next()


def create_output(headers, col_delimiter, row_delimiter):
    global headers
    headers = headers
    global col_delimiter
    col_delimiter = col_delimiter
    global row_delimiter
    row_delimiter = row_delimiter
    output = io.open('output.txt', 'wb')
    for row in info.strings:
        if isinstance(row, pbf.StringTable.sint32):
            output.write(row.string)
        elif isinstance(row, pbf.StringTable.uint32):
            output.write(row.string)
        else:
            output.write(row.string)

    output.write(row_delimiter)
   
