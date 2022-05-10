import codecs
codecs.register_error('strict', codecs.ignore_errors)

# This is a bit of a hack, but we do it anyway since we can't easily
# get the version from setup.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pysam

from pysam import Samfile, SamfileError, AlignedRead, AlignedSegment, \
     AlignmentHeader, SamtoolsError, SamtoolsVersionError, \
     SamtoolsIndexingError, TabixError, TabixIndexNotFoundError, \
     TabixIndexingError, TabixFile, TabixProperties, \
     Fastafile, FastaIndexingError, FastaFileIndexingError, \
     FastaRecord, FastaWriter, FastaWriterError, FastxFile, \
     FastxRecord, FastxWriter, FastxWriterError, FastqFile, \
     FastqRecord, FastqWriter, FastqWriterError, AlignmentFile, \
     VariantFile, VariantHeader, VariantRecord, \
     AlignmentHeader, AlignmentHeaderKey
