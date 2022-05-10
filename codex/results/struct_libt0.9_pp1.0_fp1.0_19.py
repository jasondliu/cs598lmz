import _struct

endian='<'

class PileupParser:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename)
    def parse_line(self):
        line = self.file.readline()
        if line.endswith('\n'): line = line[:-1]
        if line.endswith('\r'): line = line[:-1]
        if line == '':
            return None, None, None
        cols = line.split('\t')
        #key = line_to_key(cols)
        key = cols[:2]
        read_count = cols[3]
        bases = cols[4]
        return key, read_count, bases
    def seek(id, spos, epos):
        #query = _struct.pack(endian+'iicBIii', 0,0,id,spos>>8,spos&0xff,epos>>8,epos&0xff)
        query = _struct.pack(endian
