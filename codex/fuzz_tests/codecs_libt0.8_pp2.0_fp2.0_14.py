import codecs
codecs.encode(astr.encode('utf8'),'base64')
print(codecs.encode(astr.encode('utf8'),'base64'))

import base64
print(base64.urlsafe_b64encode(astr.encode('utf8')))
