import bz2
# Test BZ2Decompressor

with open('/tmp/enwik8', 'rb') as f:

    bz2d = bz2.BZ2Decompressor()

    print(bz2d.unconsumed_tail)
    # b''

    print(bz2d.eof)
    # False

    data = f.read(100_000)
    print(data)
    # b'<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.10/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" version="0.10" xml:lang="en">\n  <siteinfo>\n    <sitename>Wikipedia</sitename>\n    <dbname>enwiki</dbname>\n    <base>http://en.wikipedia.org/wiki/Main_Page</base>\n    <
