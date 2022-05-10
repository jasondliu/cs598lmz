import mmap

from scripts.charts.charts import Charts
from scripts.charts.constants import Constants


class FastaCharts(Charts):
    def __init__(self, data_dir, output_dir):
        Charts.__init__(self, data_dir, output_dir)

    def get_fasta_stats(self):
        fasta_file = os.path.join(self.data_dir, Constants.FASTA_FILE)
        with open(fasta_file, 'r') as f:
            mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            seq_count = 0
            seq_length = 0
            line = mm.readline()
            while line:
                if line[0] == '>':
                    seq_count += 1
                else:
                    seq_length += len(line)
                line = mm.readline()
            mm.close()
        return {
            'name': 'fasta',
            'seq_count': seq_count,

