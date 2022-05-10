import lzma
# Test LZMADecompressor on LZMA files in http://tukaani.org/lzma/benchmarks/
# See the README for details.
#
# The file x86.log.raw used for testing is a concatenation of the
# files from SUMMARY.TXT in the lzma499.tar.bz2 bundle.
#
# The file x86.rev.log.raw used for testing is the same, with each
# file in the concatenation reversed.
#
# The last file, genomedna.raw is from a project involving Joep
# P.C.E. van Gelder
# (http://bioinformatics.org/pipermail/biopython-dev/2003-June/001687.html).
#
# To create your own x86.log.raw and x86.rev.log.raw, first create
# a subdirectory named "lzma499" and unpack lzma499.tar.bz2 in it.
# Then run this script in the subdirectory containing x86, full,
# and full_bwt.

