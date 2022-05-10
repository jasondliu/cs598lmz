import weakref

from .mapping import mapping_registry
from .mapping.converter import register
from .mapping.mapping import Mapping
from .mapping.mapping import MappingBase
from .mapping.mapping import MappingConfig
from .mapping.mapping import MappingRegistry
from .mapping.mapping import MappingSections
from .mapping.mapping import MappingTree
from .mapping.mapping import Mappings
from .mapping.mapping import ProxyMapping
from .mapping.mapping import StaticMapping
from .mapping.mapping import unregister
from .mapping.mapping import unregister_all
from .utils import SingletonMeta


# mapping_registry = MappingRegistry()

