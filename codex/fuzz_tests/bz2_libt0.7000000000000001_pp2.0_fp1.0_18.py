import bz2
bz2.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# Decompress the file and store it in memory.
xmldata = bz2.decompress(bz2data)

# Print the first 1000 characters of the decompressed data.
print(xmldata[0:1000])

import re

# Extract the text using a regular expression.
text = re.findall('<text>(.*?)</text>', xmldata, re.DOTALL)

# Concatenate all of the text extracted.
whole_text = ' '.join(text)

# Print the first 500 characters.
print(whole_text[0:500])

# Tokenize the text.
tokens = nltk.word_tokenize(wh
