from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'H'
s.size = 2

data = open('sample.ogg', 'rb').read()

begin = data.find(OggSeq)

if begin == -1:
    print('Ogg sequence not found')
else:
    print('Ogg sequence found at position: %d' % begin)
    data = data[begin:]
    header = data[:s.size]
    data = data[s.size:]
    (segment_length,) = s.unpack(header)
    comment_start = segment_length + 7

    data = data[comment_start:]
    header = data[:s.size]
    data = data[s.size:]
    (segment_length,) = s.unpack(header)
    comment_end = comment_start + segment_length + s.size
    comment_data = data[:segment_length]

    # print comment data
    print('comment = %r' % comment_data)

    # skip to end of comment data
