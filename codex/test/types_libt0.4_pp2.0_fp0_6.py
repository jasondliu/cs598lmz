import types
types.ClassType = type

import unittest
import doctest

from Testing.ZopeTestCase import FunctionalDocFileSuite

from Products.CMFCore.testing import FunctionalZCMLLayer
from Products.CMFCore.tests.base.testcase import SecurityTest
from Products.CMFCore.tests.base.tidata import FTIDATA_CMF15
from Products.CMFCore.tests.base.tidata import FTIDATA_CMF16
from Products.CMFCore.tests.base.tidata import FTIDATA_CMF20
from Products.CMFCore.tests.base.tidata import STI_CMF15
from Products.CMFCore.tests.base.tidata import STI_CMF16
from Products.CMFCore.tests.base.tidata import STI_CMF20

from Products.CMFCore.TypesTool import FactoryTypeInformation as FTI
from Products.CMFCore.TypesTool import ScriptableTypeInformation as STI

