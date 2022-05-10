import _struct
import mmap
import os

from dlm.abstract import IDownloadManager
from log import LogSupport
from names import Names
from ..common import _REQUEST_TYPE, _FILE_SECTION, _SECTION_TYPE, _FILE_SECTION_ACTION, _FILE_SECTION_RESPONSE, _FILE_SECTION_ERROR_CODE
from ..common import _FILE_SECTION_ERROR_CODE_NO_ERROR
from ..common import _FILE_SECTION_ERROR_CODE_INTERNAL_ERROR
from ..common import _FILE_SECTION_ERROR_CODE_INVALID_REQUEST
from ..common import _FILE_SECTION_ERROR_CODE_INVALID_AGENT_ID
from ..common import _FILE_SECTION_ERROR_CODE_INVALID_RESOURCE_ID
from ..common import _FILE_SECTION_ERROR_CODE_INVALID_SECTION_ID
from ..common import _FILE_SECTION_ERROR_CODE_NOT_ENOUGH_RESOURCES
from ..common import _FILE_SECTION_ERROR
