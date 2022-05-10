import lzma
lzma.LZMACompressor(format=1)
#
#
# # find prefix of input file
# file_pref = os.path.split(f_in)[1].split('.')[0]
# # Create the output file name by inserting .out between .xz and .files
# f_out = f_in.replace(".xz",".out")
#
# # Create an LZMA compressor object
# compressor = lzma.LZMACompressor()
#
# # Read a portion of the input file into an input buffer
# with open(f_in,'rb') as fin:
#     data = fin.read(65536)
#
# # Open the output file for writing
# with open(f_out,'wb') as fout:
#     # While there is still data to be compressed
#     while data:
#         # Call the compressor object to compress the data; it returns the
#         # compressed data
#         compressed = compressor.compress(data)
#         # Write the compressed data to the output file
#         fout.write(compressed
