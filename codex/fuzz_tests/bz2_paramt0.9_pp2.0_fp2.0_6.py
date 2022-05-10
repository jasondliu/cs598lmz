from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = handle_bz2_eof

from email import parser
import email
import sys
import os
import tarfile

# import Apache Lucene
# from org.apache.pylucene.analysis import PythonAnalyzer
# from org.apache.lucene.analysis import WhitespaceTokenizer
# from org.apache.lucene.analysis import TokenFilter
# from org.apache.lucene.analysis import TokenStream
# from org.apache.lucene.analysis import StopFilter
# from org.apache.lucene.analysis import Analyzer
# from org.apache.lucene.analysis import CharArraySet
# from java.io import StringReader


# import nettle
# from nettle import nettle_cipher
# from nettle import nettle_cbc
# from nettle import get_key
# from nettle import get_IV

# import zlib
#
#
# # ZDecompressor = zlib.decompressobj().decompress
#
#
# ########################################################
# #                        UTILS                         #
# #################################
