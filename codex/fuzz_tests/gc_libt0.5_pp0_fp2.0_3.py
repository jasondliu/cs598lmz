import gc, weakref

from brian2.utils.logger import get_logger
from brian2.utils.stringtools import get_identifiers
from brian2.core.preferences import prefs
from brian2.core.variables import Variables
from brian2.core.namespace import get_local_namespace
from brian2.core.functions import DEFAULT_FUNCTIONS
from brian2.core.clocks import Clock
from brian2.core.scheduler import Scheduler
from brian2.core.network import Network
from brian2.core.magic import register_class, BrianObject
from brian2.core.names import Nameable
from brian2.core.preferences import brian_prefs
from brian2.core.spikesource import SpikeSource
from brian2.core.base import weakproxy_with_fallback
from brian2.core.magic import BrianPreference
from brian2.core.magic import doc_restrict
from brian2.core.magic import doc_deprecated_alias
from brian2.core
