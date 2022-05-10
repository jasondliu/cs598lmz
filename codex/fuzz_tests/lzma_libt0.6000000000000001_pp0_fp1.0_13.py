import lzma
lzma.open()

from aioconsole import ainput, aprint

from .utils import (
    aexec,
    get_access_token,
    get_authorization_url,
    get_code,
    get_refresh_token,
    get_token,
    get_token_dict,
    request_token,
    save_token,
)

from .download import download
from .upload import upload


class Arvados:

    def __init__(self, host=None, token=None, client_id=None, client_secret=None,
                 **kwargs):
        """
        Arvados client class

        Arguments:
            host: Arvados cluster hostname.
            token: User's API token.
        """
        self.host = host
        self.token = token
        self.client_id = client_id
        self.client_secret = client_secret

        if not self.host:
            self.host = os.environ.get('ARVADOS_API_HOST')
            if not self.
