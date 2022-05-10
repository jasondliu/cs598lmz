from lzma import LZMADecompressor
LZMADecompressor().decompress(f.read())
</code>
The <code>.json</code> file contains the below text:
<code>{'md5': '0c10b7f5ef9e1f90b8b5d5b06e5bab28', 'original_id': 'espn_v1.1', 'original_url': 'http://api.espn.com', 'tables': [{'columns': ['id', 'division', 'league', 'name', 'shortName', 'records'], 'contents': [[1, 1, 1, 'Baltimore Orioles', 'BAL', [0, 0, 0], 1], [2, 1, 1, 'Boston Red Sox', 'BOS', [0, 0, 0], 2], [3, 1, 1, 'New York Yankees', 'NYY', [0, 0, 0], 3], [4, 1, 1, 'Tampa Bay Rays', 'TB', [0, 0, 0], 4], [5, 1, 1, 'Toronto Blue Jays', 'TOR', [0, 0, 0], 5], [6, 2
