from lzma import LZMADecompressor
LZMADecompressor.decompress(data2[0])

#Lets observe the list.
for i in data2:
    print(f"{type(i)}: {i[:10]} {i[-10:]}")
    break

#Looks like xml content. But its not.

#Lets observe each xml_part individually.
for count, i in enumerate(data2):
    s = LZMADecompressor.decompress(i)
    print(count)
    try:
        print(f"{type(ET.fromstring(s))}")
    except ET.ParseError as e:
        print(repr(e))
    except ET.ParserError as e:
        print(repr(e))
    finally:
        print()

#None of the data is tag.
# This means there are two types of data in xml_parts.

"""
data:  <xml feedVersion="3" type="some" feeid="20">
<env:Envelope xmlns:env="http://www.w3.org/2003/05
