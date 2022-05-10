import bz2
# Test BZ2Decompressor.__init__ and BZ2Decompressor.private_init
with bz2.BZ2Decompressor(bz2.decompress(b"BZh10AY&SYÃ`Â\x14\x00\x00Ã\x019N")) as bz:
    bz.decompress(b"BZh10AY&SYÃ`Â\x14\x00\x00Ã\x019N")
KEYS1 = {'foo': {'id': 'bar'},
 'foo2': {'id': 'bar2'},
 'frob': {'id': 'oof'},
 'rab': {'id': 'oof'},
 'rabcf': {'id': 'rabcf'},
 'rabcf1': {'id': 'rabcf'},
 'rabcf2': {'id': 'rabcf'},
 'rabcf3': {'id': 'rabcf'},
 'rabcf4': {'id': 'rabcf'},
 'rabcf5': {'id': 'rabcf'},
 'rabcf
