import gc, weakref
import warnings

from numpy.testing import assert_array_equal

from spyder.utils.qthelpers import qapplication
from spyder.utils.programs import is_module_installed
from spyder.widgets.variableexplorer.collectionseditor import (
    CollectionsEditorTableView)
from spyder.widgets.variableexplorer.tests.base import (
    setup_item, teardown_item, CollectionsEditorTestCase)

#==============================================================================
# Utility functions
#==============================================================================
def get_view(editor, index):
    """
    Return the view for the given *index*
    """
    return editor.views[index.parent()][index.row()]


def get_editor(editor, index):
    """
    Return the editor for the given *index*
    """
    return get_view(editor, index).editor


def get_item(editor, index):
    """
    Return the item for the given *index*
    """
    return editor.model.data(index, Qt.UserRole)


def get_value(editor,
