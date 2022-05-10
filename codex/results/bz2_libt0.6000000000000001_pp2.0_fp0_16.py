import bz2
bz2.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

#The bz2 module provides a comprehensive interface for the bz2 compression library. It implements a complete file interface, one shot (de)compression functions, and types for sequential (de)compression.

#The module consists of two primary objects and a handful of auxiliary types and functions.

#bz2.BZ2Compressor([compresslevel])

#Return a compressor object, to be used for compressing data streams that won’t fit into memory at once.

#The compresslevel parameter, if given, must be a number between 1 and 9.

#The compresslevel parameter is ignored if the compresslevel keyword argument is given when calling the compressor’s compress() or flush() method.

#bz2.BZ2Dec
