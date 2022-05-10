from lzma import LZMADecompressor
LZMADecompressor()
from gzip import GzipFile

def read_fasta(filename):
    seq_records = []
    with open(filename, 'r') as fp:
        for line in fp:
            line = line.strip()
            if (line[0] == ">"):
                if (len(seq_records) == 0):
                    seq_records.append([line, ""])
                else:
                    if (seq_records[-1][1] != ""):
                        seq_records[-1] = (seq_records[-1][0], "".join(seq_records[-1][1]))
                    seq_records.append([line, ""])
            else:
                seq_records[-1][1] += line.upper()
    return seq_records


class mz_spectrum:
    def __init__(self, ms_type, peak_intensity_threshold, peak_filtering_window_size, peak_filtering_window_step_size,
                 peak_filtering_method, charge
