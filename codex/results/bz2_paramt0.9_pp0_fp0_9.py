from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(sys.argv[1])
print(BZ2Decompressor())

# For example, use the following command:
# ./bz2regex.py BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084

# Please report any findings to rjuly@mozilla.com by 12/21/09.
# 
# Reward Points: 7.3
# 
# Explanation: This is an example of a command injection vulnerability, similar to 95.
#
# Solution
# 
# cat flag | python bz2regex.py "BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00\x00!\x9ah3M\x07<
