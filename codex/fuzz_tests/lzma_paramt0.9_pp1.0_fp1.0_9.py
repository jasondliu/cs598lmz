from lzma import LZMADecompressor
LZMADecompressor = None

# Set default logging handler to avoid "No handler found" warnings.
from logging import NullHandler

from .stream import Stream, __all__ as _stream_all
from .block import Block, __all__ as _block_all
from .frame import Frame, __all__ as _frame_all
from .ancillary import (
    AncillaryData, __all__ as _ancillary_data_all,
    NonDegenerateAncillaryData, __all__ as _non_deg_ancillary_data_all,
    NondegenerateAncillaryData, __all__ as _nondeg_ancillary_data_all,
    DegenerateAncillaryData, __all__ as _deg_ancillary_data_all,
    AncillaryResource, __all__ as _ancillary_resource_all,
    AncillaryResourceIdentifier, __all__ as _ancillary_resource_identifier_all,
    AncillaryUsageInformation, __all__ as _ancillary_usage_information_all,
    AncillaryResourceFormatInformation, __all__ as _anc
