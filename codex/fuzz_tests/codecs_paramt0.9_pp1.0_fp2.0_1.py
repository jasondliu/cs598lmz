import codecs
codecs.register_error("strict", codecs.replace_errors)

from savReaderWriter import SavReader
from pandas import DataFrame
from savReaderWriter import SavWriter

# ------------------------------------------------------------------------

if len(sys.argv) != 3:
    print("usage: sav2ddi.py sav-file ddi-file")
    sys.exit(1)

# ------------------------------------------------------------------------

in_file = sys.argv[1]
out_file = sys.argv[2]

reader = SavReader(in_file)
reader.ioUtf8 = True
df = DataFrame(list(reader))

# ------------------------------------------------------------------------

with SavWriter(out_file, df) as writer:
    pass
