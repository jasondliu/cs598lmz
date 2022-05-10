import bz2
bz2.decompress(part2).decode()

with bz2.BZ2File("example3.xml.bz2") as xml_file:
    doc = xmltodict.parse(xml_file.read())

