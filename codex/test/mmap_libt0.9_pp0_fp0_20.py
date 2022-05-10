import mmap
import re
from StringIO import StringIO

from gt.compat import PY3K
from gt.extended.genome_stream import GFF3InStream, GFF3OutStream
from gt.extended.genome_node import FeatureNode, RegionNode


class TestGFF3InStream(TestCase):

    def setUp(self):
        self.gff3_dir = os.path.join(os.path.dirname(__file__), "gff3_files/")
        self.test_files = ["samples.gff3",
                           "refseq.gff3",
                           "gvf.gff3",
                           "multiple_whitespace.gff3"]

    def test_header(self):
        test_stream = GFF3InStream(os.path.join(self.gff3_dir,
                                                self.test_files[1]))
