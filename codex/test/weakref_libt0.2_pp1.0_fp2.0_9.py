import weakref

from PyQt5.QtCore import QObject, QTimer, pyqtSignal

from UM.Application import Application
from UM.Logger import Logger
from UM.PluginRegistry import PluginRegistry
from UM.Settings.ContainerRegistry import ContainerRegistry
from UM.Settings.DefinitionContainer import DefinitionContainer
from UM.Settings.InstanceContainer import InstanceContainer
from UM.Settings.ContainerStack import ContainerStack
from UM.Settings.Interfaces import ContainerInterface
from UM.Settings.SettingDefinition import SettingDefinition
from UM.Settings.SettingFunction import SettingFunction
from UM.Settings.SettingRelation import SettingRelation
from UM.Settings.Validator import Validator
from UM.Settings.ContainerStack import ContainerChangedMessage
from UM.Settings.ContainerStack import InvalidContainerStackError
from UM.Settings.ContainerStack import ContainerStackChangedMessage
from UM.Settings.ContainerStack import PropertyChangedMessage
from UM.Settings.ContainerStack import ContainerPropertyChangedMessage
from UM.Settings.ContainerStack import ContainerStackPropertyChangedMessage
from UM.Settings.ContainerStack import ContainerStackValidationStateChangedMessage
