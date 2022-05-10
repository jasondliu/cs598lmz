import weakref

from lxml import etree

from .base import BaseElement
from . import _base_types as base_types
from . import _utils
from . import _utils as utils
from . import _utils_ns
from . import xades


class Timestamp(BaseElement):
    """
    Class for Timestamp elements.

    Args:
        tst_type (str): Type of timestamp. Can be one of the following:
            - `all`: all the data objects in the signature
            - `signature`: the signature value
            - `signature-certificate`: the certificate or certificate chain
              used to sign the signature
            - `signature-crl`: the CRL used to verify the signature
            - `signature-timestamp`: the timestamp element itself
            - `refs-only`: the references present in the signature
            - `refs-only-complete`: the references present in the signature
              and the complete certificate chain
            - `archive`: the archive timestamp
        tst_info (TimestampInfo): Timestamp info.
        encoding (str
