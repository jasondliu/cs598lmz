import types
types.ClassType = type

import sys
import os
sys.path.append(os.path.abspath(os.path.pardir))

import unittest

from lxml import etree

from pcs.lib.cib.tools import find_unique_id
from pcs.lib.cib.tools import find_element_by_tag_and_id
from pcs.lib.cib.tools import find_element_by_tag_and_attr_value
from pcs.lib.cib.tools import find_element_by_tag_and_attrs_list
from pcs.lib.cib.tools import find_first_child_element_by_tag
from pcs.lib.cib.tools import find_first_element_by_tag_and_attribute
from pcs.lib.cib.tools import get_attribute_value
from pcs.lib.cib.tools import get_attribute_values
from pcs.lib.cib.tools import get_child_nodes_by_tag
from pcs.lib.cib.tools import
