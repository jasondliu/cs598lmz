import mmap
import uuid
from typing import List, Optional, Union

from ..exceptions import (
    AirbrakeAPIError,
    AirbrakeAPIException,
    AirbrakeAPIHTTPError,
    AirbrakeAPIRequestError,
)
from ..response import AirbrakeResponse
from ..types import AirbrakeNotices, AirbrakeNotice


url_t = Union[str, bytes, Path, IO]
RESPONSE_CONTENT_TYPE = "application/json"


class AirbrakeRequest:
    """This class represents an Airbrake request."""

    def __init__(self, base_url: str, **kwargs):
        """Initialize Airbrake request.

        Args:
          base_url: Airbrake API URL.
          kwargs: the keyword arguments.
        """
        self.api_key = kwargs.pop("api_key")
        if not self.api_key:
            raise AirbrakeAPIException("Airbrake's API key required")
