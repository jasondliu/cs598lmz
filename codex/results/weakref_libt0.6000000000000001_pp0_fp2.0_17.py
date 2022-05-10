import weakref

from core import exceptions
from core.objects.svcdict import KEYS
from core.objects.svcdict import SvcDict
from utilities.lazy import lazy
from utilities.string import bdecode
from utilities.string import bencode
from utilities.string import is_string
from utilities.string import is_string_set
from utilities.string import is_stringish
from utilities.string import is_stringlike
from utilities.string import is_valid_ip
from utilities.string import is_valid_name
from utilities.string import is_valid_port
from utilities.string import is_valid_service
from utilities.string import is_valid_service_list
from utilities.string import is_valid_service_name
from utilities.string import is_valid_service_name_list
from utilities.string import is_valid_service_port
from utilities.string import is_valid_service_port_list
from utilities.string import is_valid_service_port_name
from utilities.string import is_valid_service_port_name_list
from utilities.string import is_valid_service_port
