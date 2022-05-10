import codecs
codecs.open('myencode.py', 'w', 'utf-8')

# Instead of passing in utf-8 each time, create a wrapper and point it towards the module codecs
import codecs
import encodings

def lookuptable():
	return codecs.lookup('utf-8'), codecs.utf_8_encode, codecs.utf_8_decode 

codecs.register(lookuptable)

# Utf-7 is one of utf's oldest and most unique options. It was design to be a more efficient way to store text. 
# It stores files in a Base64 format
# ASCII characters encoded in regular Ascii and everything else as + symbols then encoded as base64
# Commonly used by MSN messenger
# Although it's old and weird, it might be common in some data sets, so you should be prepared

# There are multiple ways to convert strings to base64, but there are also modules that can be called
# use the b64encode() method
import base64
encoded = base64.b64encode('encode me!')
print
