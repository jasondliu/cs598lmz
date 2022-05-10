import _struct

from . import _compat
from . import _util
from . import _vendor
from . import _vendor_packages

_logger = _util.get_logger(__name__)

_vendor.add_directory(_vendor_packages.__path__[0])

_vendor.import_module('google.protobuf.descriptor_pb2')
_vendor.import_module('google.protobuf.message_factory')
_vendor.import_module('google.protobuf.reflection')
_vendor.import_module('google.protobuf.service')
_vendor.import_module('google.protobuf.service_reflection')
_vendor.import_module('google.protobuf.symbol_database')
_vendor.import_module('google.protobuf.text_format')
_vendor.import_module('google.protobuf.internal.api_implementation')
_vendor.import_module('google.protobuf.internal.containers')
_vendor.import_
