import socket
import ssl

import requests


class BaseUrl(object):
    """Base class for urls."""

    def _get_headers(self):
        """Returns the headers for the request.

        Returns:
            dict: The headers.
        """
        return {}

    def _get_params(self):
        """Returns the params for the request.

        Returns:
            dict: The params.
        """
        return {}

    def _get_data(self):
        """Returns the data for the request.

        Returns:
            dict: The data.
        """
        return {}

    def _get_cookies(self):
        """Returns the cookies for the request.

        Returns:
            dict: The cookies.
        """
        return {}

    def _get_timeout(self):
        """Returns the timeout for the request.

        Returns:
            tuple: The timeout.
        """
        return (None, None)

    def _get_proxies(self):
        """Returns the proxies for the request.

        Returns:
            dict: The proxies.

