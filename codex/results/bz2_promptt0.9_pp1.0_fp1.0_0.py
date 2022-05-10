import bz2
# Test BZ2Decompressor
# data_decompressed = bz2.decompress(data)
data_decompressed = bz2.BZ2Decompressor().decompress(data)
data_decompressed = str(data_decompressed, encoding='utf-8')
print(f"Data Decompressed: {len(data_decompressed)}")
print(data_decompressed[:100].replace('\n', '_'))
print(data_decompressed[:100].replace('\n', '_'))

# Regex Features
import re
pattern = r"the"
re.findall(pattern, data_decompressed)
len(re.findall(pattern, data_decompressed))
pattern = r"the"
matches = re.search(pattern, data_decompressed)
print(matches)
matches = re.match(pattern, data_decompressed)
print(matches)
regex = r"the"
pattern = re.compile(regex)
matches = pattern.findall(data_decompressed)
