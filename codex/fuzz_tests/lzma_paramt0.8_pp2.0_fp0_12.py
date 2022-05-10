from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self, ndata=None, skipdata=None: BZ2Decompressor.flush(self, ndata, skipdata)
</code>
The actual base64 encoded data string is:
<code>'eJyNkU+I2UQgNhQxgUjBs4U6BgU6ZkT29BnjHYDYwYCrjzgvEObx0H0XLuOJbFZpbBAjQQeAaMg0hYkYlJBDvR8jxO5LA5QtQeCIRVDqO8WixkWTpfnYwA0KKm1M8RxEW5cL9tAStFtqZ3oKZWtJmhBmhDpCzpGWxgW/PUXFFkxP/LRrPZ2MRFbYc1fNrYezUeB6QzLgU53KsU4I6ZsTdTOL0BT0KwbSZYHrxzFq3
