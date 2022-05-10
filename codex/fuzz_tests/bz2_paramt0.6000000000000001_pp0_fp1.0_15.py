from bz2 import BZ2Decompressor
BZ2Decompressor.__init__ = lambda x: None

from bz2 import BZ2Compressor
BZ2Compressor.__init__ = lambda x: None

from bz2 import BZ2File
BZ2File.__init__ = lambda x: None

from bz2 import bz2_decompress
bz2_decompress.__init__ = lambda x: None

from bz2 import bz2_compress
bz2_compress.__init__ = lambda x: None

from bz2 import compress
compress.__init__ = lambda x: None

from bz2 import decompress
decompress.__init__ = lambda x: None

from bz2 import open
open.__init__ = lambda x: None
