import weakref

from . import _cffi_backend
from ._cffi_backend import (
    _CData, _CDataMeta, _CDataOwned, _CDataOwnedMeta, _CDataGCP, _CDataGCPMeta,
    _CDataMeta_set_c_type, _CDataMeta_set_c_data, _CDataMeta_set_c_data_finalizer,
    _CDataMeta_set_c_data_no_finalizer, _CDataMeta_set_c_data_no_finalizer_or_type,
    _CDataMeta_set_c_data_no_finalizer_or_type_or_b_needsfree,
    _CDataMeta_set_c_data_no_finalizer_or_b_needsfree,
    _CDataMeta_set_c_data_no_finalizer_or_b_needsfree_or_type,
    _CDataMeta_set_c_data_no_finalizer_or_b_needsfree_or_type_or_gc,
    _
