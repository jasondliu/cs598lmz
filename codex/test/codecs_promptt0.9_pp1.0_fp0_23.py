import codecs
# Test codecs.register_error('test', codec_test_patched)

# http://codereview.stackexchange.com/questions/41230/decode-utf-8-error-using-unicode-xml-in-python-2-7
import xml.etree.cElementTree as ET
ET.register_namespace('newxmlns',"http://www.opengis.net/wfs")
ET.register_namespace('','http://www.opengis.net/wfs')
ET.register_namespace('xlink','http://www.w3.org/1999/xlink')
ET.register_namespace('gml','http://www.opengis.net/gml')
ET.register_namespace('xsi','http://www.w3.org/2001/XMLSchema-instance')

#
buf = 'handle_text(u"&#x02306d2;", 0, 7)'
print(buf)
