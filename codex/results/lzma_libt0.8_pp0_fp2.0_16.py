import lzma
lzma.have_lzma()

import tarfile
tar = tarfile.open("output.tar.xz", "w:xz")
tar.add("/tmp/foo")
tar.add("/tmp/bar/baz")
tar.close()
