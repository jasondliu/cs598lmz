import weakref

from pymel import versions
from pymel.util.arguments import getArgument
from pymel.util.decoration import decorator

from pymel.internal.pmcmds import addExtension
from pymel.internal.pmcmds import removeExtension
from pymel.internal.pmcmds import renameExtension
from pymel.internal.pmcmds import extension
from pymel.internal.pmcmds import exists
from pymel.internal.pmcmds import setParent
from pymel.internal.pmcmds import match
from pymel.internal.pmcmds import xform
from pymel.internal.pmcmds import delete
from pymel.internal.pmcmds import parent
from pymel.internal.pmcmds import listRelatives
from pymel.internal.pmcmds import listConnections
from pymel.internal.pmcmds import getAttr
from pymel.internal.pmcmds import setAttr
from pymel.internal.pmcmds import addAttr
