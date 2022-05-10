import socket
import time
import unittest

from src.sc.pwr.inz.memory.LongTermMemory.loadSave import LoadSaveJSON
from src.sc.pwr.inz.memory.LongTermMemory.semantic.identifiers.Trait import Trait
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Formula import Formula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.State import State
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.TraitType import TraitType
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.View import View
from src.sc.pwr.inz.memory.LongTermMemory.semantic.maps.HebbianMap import HebbianMap
from src.sc.pwr.inz.memory.LongTermMemory.semantic.maps.IdentifierMap import IdentifierMap
