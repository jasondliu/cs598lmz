import gc, weakref
from . import custom_exceptions as exc

CONTIG_NAMING_SCHEME = "Illumina"

def get_readvector_factory():
    return ReadVectorFactory(CONTIG_NAMING_SCHEME)


class ReadVectorFactory(object):
    
    def __init__(self, contig_naming_scheme):
        self.contig_naming_scheme = contig_naming_scheme
        self.cache = dict()
        self.last_contig = ""
    
    def clear_cache(self):
        self.cache = dict()
    
    def get_readvector(self, contig, read_name, strand, start, end, mate_start, mate_end, mapped):
        if contig != self.last_contig:
            self.cache.clear()
            self.last_contig = contig
        if (read_name, strand, start, end, mate_start, mate_end, mapped) in self.cache:
            return self.cache[(read_name, strand
