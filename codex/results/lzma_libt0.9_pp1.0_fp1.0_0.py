import lzma
lzma_open = lzma.open
except:
    lzma_open = None
    
try:
import gzip
gzip_open = gzip.open
except:
    gzip_open = None
    
try:
import bz2
bz2_open = bz2.open
except:
    bz2_open = None
    
def smart_open(file,*args,**kwargs):
    if file.endswith('.gz'):
        opener = gzip_open
    elif file.endswith('.bz2'):
        opener = bz2_open
    elif file.endswith('.xz'):
        opener = lzma_open
    else:
        opener = open
    if opener is None:
        # Fallback to python's built in open
        opener = open
    return opener(file,*args,**kwargs)

class Vcf(object):
    """ This class is a handle for a tabix indexed VCF.
    """
    def __init__(self, filename
