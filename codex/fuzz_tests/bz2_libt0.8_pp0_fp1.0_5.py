import bz2
bz2.BZ2File(filename, 'w')

"""
    for i in range(len(args)):
        if not isinstance(args[i], str):
            raise TypeError('arguments must be string')
            return
    if not isinstance(bz2file, bz2.BZ2File):
        raise TypeError('must provide object of type bz2.BZ2File')
        return
    bz2file.write('\n'.join(args)+'\n')

def bz2write_line(bz2file, *args):
    for i in range(len(args)):
        if not isinstance(args[i], str):
            raise TypeError('arguments must be string')
            return
    if not isinstance(bz2file, bz2.BZ2File):
        raise TypeError('must provide object of type bz2.BZ2File')
        return
    bz2file.write('\n'.join(args)+'\n')

def bz2close(bz2file):
   
