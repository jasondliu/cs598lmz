from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("./data/enwiki-latest-pages-articles.xml.bz2",'rb').read())[:60]

# <mediawiki xmlns="http://www.mediawiki.org/xml/export-0.10/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" version="0.10" xml:lang="en">
# <siteinfo>
# <sitename>Wikipedia</sitename>
# <dbname>enwiki</dbname>
# <base>http://en.wikipedia.org/wiki/Main_Page</base>
# <generator>MediaWiki 1.21wmf1</generator>
# <case>first-letter</case>
# <namespaces>
# <namespace key="-2" case="first-letter">Media</namespace>
# <namespace key="-1
