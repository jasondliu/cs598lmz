from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = fixed_decompress


class Client(object):
    """
    A thin wrapper around the REST API.
    """

    def __init__(self, url, *args, **kwargs):
        """
        The url should be the url to the root of the HTTPD, with no trailing
        slash.
        """

        if not url.endswith('rest'):
            url = url.rstrip('/') + '/rest/'

        self.base_url = url
        self.session = requests.session(*args, **kwargs)

    #
    # Utilities
    #

    @staticmethod
    def _check_status(response):
        """
        Check the given response for an abort-worthy HTTP code; if so, raise an
        appropriate HTTPError.
        """

        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            if response.status_code == codes.unauthorized:
                raise UnauthorizedError(response, e)
            else:
                raise

    @staticmethod
    def
