import weakref
import collections

from gi.repository import GtkSource, Gtk, GObject
from sugar3 import mime
from sugar3.bundle.activitybundle import get_bundle_path


class Editor(GtkSource.View):

    expected_mime_types = ['text/plain', 'text/html']
    mybundle = get_bundle_path()
    file_type = 'plain'

    def __init__(self, parent=None, shrink_button=True, **kwargs):
        GtkSource.View.__init__(self, parent, **kwargs)

        self._buffer = GtkSource.Buffer()
        self.set_buffer(self._buffer)

        self._tab_width = 4

        self._buffer.set_highlight_matching_brackets(True)
        self._buffer.set_max_undo_levels(1000)

        self.set_auto_indent(True)
        self.set_indent_on_tab(True)
        self.set_insert_spaces_instead_of_tabs
