import gc, weakref
import logging

from . import utils, config, exceptions
from .utils import get_module_name
from .config import get_config
from .exceptions import (
    HttpError,
    HttpBadRequestError,
    HttpUnauthorizedError,
    HttpForbiddenError,
    HttpNotFoundError,
    HttpMethodNotAllowedError,
    HttpConflictError,
    HttpRequestEntityTooLargeError,
    HttpUnsupportedMediaTypeError,
    HttpServerError,
    HttpServiceUnavailableError,
    HttpGatewayTimeoutError,
    HttpVersionNotSupportedError,
    HttpInvalidHeaderError,
    HttpInvalidHeaderName,
    HttpInvalidHeaderValue,
    HttpInvalidURL,
    HttpTooManyRedirects,
    HttpInvalidBodyType,
    HttpInvalidChunkSize,
    HttpInvalidProxyURL,
    HttpInvalidProxyScheme,
    HttpInvalidScheme,
    HttpInvalidURL,
    HttpInvalidHeader,
    HttpInvalidHeaderValue
