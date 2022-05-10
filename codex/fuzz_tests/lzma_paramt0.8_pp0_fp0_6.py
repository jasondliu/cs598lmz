from lzma import LZMADecompressor
LZMADecompressor().decompress(final_ans)

#%%

#%%
# Packet Design
#%%
# Packet Format
#%%
# Each packet contains 4 bytes header and 0-2047 bytes of data.
#
# Header is encoded as a 32-bit little-endian integer.
#
# Bits 0-15 encode the packet sequence number modulo 2**16.
# Bits 16-23 encode the packet data length, capped at 2**11.
# Bits 24-31 are reserved and must be set to 0.
#
# Each packet contains up to 2**11=2048 bytes of data, and the data is encoded
# as raw bytes.
#%%

#%%
payload = zlib.compress(LZMADecompressor().decompress(final_ans))
seq_num = 0

pktList = []
pktCount = {}

for i in range(len(payload) // 2048 + 1):
    pkt = struct.pack('<I', seq_num) + payload[i*2048: (i+1)*2048]
    pktList
