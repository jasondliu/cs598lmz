import mmap
import os
import sys
import time

from collections import OrderedDict

from aiida.common.exceptions import NotExistent
from aiida.common.utils import classproperty
from aiida.orm.data.base import Str, Float, Int, Bool, List, Dict, to_aiida_type
from aiida.orm.data.parameter import ParameterData
from aiida.orm.data.structure import StructureData
from aiida.orm.data.singlefile import SinglefileData
from aiida.orm.utils import DataFactory
from aiida.plugins import DataFactory as PluginFactory
from aiida.orm.data.base import Data
from aiida.orm.data.folder import FolderData
from aiida.orm.data.remote import RemoteData
from aiida.orm.data.array.kpoints import KpointsData
from aiida.orm.data.array.trajectory import TrajectoryData
from aiida.orm.data.array.modes import ModesData
from aiida.orm.data.
