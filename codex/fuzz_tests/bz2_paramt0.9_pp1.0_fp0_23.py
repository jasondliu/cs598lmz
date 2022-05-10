from bz2 import BZ2Decompressor
BZ2Decompressor = BZ2Decompressor

import pyrax

from pygments.lexers.shell import BashLexer
from django.utils.safestring import mark_safe


class DjangoRax:
    '''
    This class works as a container for all Rackspace servers that Django should
    use. It also collects object storage containers and interacts with cloud
    files, such as creating the "cors" headers.
    '''

    def __init__(self, settings_module=None):
        self.nova = None
        self.pyrax = None
        self.cf = None
        self.identity_type = 'rackspace'
        self.endpoint = None
        self.username = None
        self.api_key = None
        self.region = None
        self.setup(settings_module=settings_module)

    def authenticate(self):
        self.pyrax.set_setting('identity_type', self.identity_type)
        self.pyrax.set_credentials(self.username, self.api_key, region=self.region)
       
