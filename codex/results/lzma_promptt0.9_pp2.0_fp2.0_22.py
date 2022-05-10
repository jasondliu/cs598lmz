import lzma
# Test LZMADecompressor    
with open('fbo-official-feed.xml', 'rb') as fh:
#     decompressor = LZMADecompressor()
    for chunk in fh:
        print(len(chunk))
        break
#         print(decompressor.decompress(chunk))
    
    
    
    

def __clear_head__(line):
    line = line[len('fbo_indian_xml '):]
    line = line[:line.index(' ')]
    line = line[:line.rindex(']')]
    return line
    
    
    
def __clear_date__(line):
    ind = line.rindex(']')
    return line[:ind + 1]

def __clear_tail__(line):
    while line and line[-1] not in '0123456789':
        line = line[:-1]
    return line

def __parse_fields__(fields):
    out_f = {}
    for field in fields:
        if field:
            field = field.
