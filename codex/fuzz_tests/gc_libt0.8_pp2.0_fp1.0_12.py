import gc, weakref

import wx
from wx.lib.masked import NumCtrl

from bric_type import *
from bric_data import *
from bric_dialog import *

from bric_spec_base import *
from bric_spec_field import *
from bric_spec_record import *

from bric_util import *

#-------------------------------------------------------------------------------
# Begin Class SpecList
class SpecList(SpecBase):
    r"""
    List type specification.
    """
    _class_name = 'List'
    _attr_type = 'list'
    _attr_list_type = None
    _attr_length = 0

    #---------------------------------------------------------------------------
    # Begin Class HTML
    class HTML(SpecBase.HTML):
        """
        Class for rendering HTML for a list type.
        """

        #-----------------------------------------------------------------------
        # Override Method: get_content
        def get_content(self, spec):

            # Create HTMLTable
            table = wx.html.HtmlTable(1+len(spec.get_fields()), 2)
            table.SetBorder
