import mmap
import os
import datetime
import zlib


def get_cached_data(root_folder, db_file, dbname, use_cache, _type):
    #def get_sequence_data(db_file, use_cache):
    """Load sequence data, as dict with keys:
    'len', 'var', 'snps', 'refseq', 'aseq', 'date', 'bases'
    """
    db_file = os.path.join(root_folder, dbname, db_file)
    data_file = db_file.replace('.db', '.dat')
    seq_file = db_file.replace('.db', '.fas')
    if not use_cache or not os.path.exists(data_file):
        # test to see if recent data file exists
        if os.path.exists(seq_file):
            print("no cached %s data for %s, making from fasta file"%(
                    _type, os.path.splitext(db_file)[0]))
            # do a new analysis
            sequence
