import lzma
# Test LZMADecompressor
#lzc = lzma.LZMADecompressor()

#result_string = lzc.decompress(f.read())

#with open('/tmp/result_string','wb') as r:
#    r.write(result_string)

#    r.close()
#    f.close()
# Indexing

# Track each "level" in the indexing file to fill the specific elements of the dict

tmp_name = list()
tmp_order = list()
tmp_first = list()
tmp_last = list()
tmp_length = list()
level = 0;
for line in f:
        line = line.strip()
        if level == 0:
                # Only entry in this file
#                print('---- Level ' + str(level) + ' is being processed ----')
#                print('---- Name: ' + line)
                tmp_name.append(line)
#                print('---- Complete ----')
                level += 1
                continue
        elif level == 1:
#                print('---- Level ' + str(level)
