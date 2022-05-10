import lzma
lzma.LZMAError

import os
os.path.abspath('.')
os.path.abspath('..')
os.path.abspath('/')
os.path.abspath('/tmp')
os.path.abspath('/tmp/')
os.path.abspath('/tmp/../')
os.path.abspath('/tmp/../../')
os.path.abspath('/tmp/../../../')
os.path.abspath('/tmp/../../../..')
os.path.abspath('/tmp/../../../../')
os.path.abspath('/tmp/../../../../..')
os.path.abspath('/tmp/../../../../../')
os.path.abspath('/tmp/../../../../../..')
os.path.abspath('/tmp/../../../../../../')
os.path.abspath('/tmp/../../../../../../..')
os.path.abspath('/tmp/../../
