import weakref

from gi.repository import GLib, Gtk, Pango, GObject

from gaphor.core.modeling import Presentation
from gaphor.core.styling import Styling
from gaphor.diagram.diagramtools import DiagramTools
from gaphor.diagram.text import FontWeight, FontStyle
from gaphor.diagram.textedit import TextEditor
from gaphor.diagram.textedit.textbuffer import TextBuffer
from gaphor.diagram.textedit.textview import TextView
from gaphor.diagram.textedit.textlayout import TextLayout


@Gtk.Template(resource_path='/org/gaphor/ui/diagramtextitem.ui')
class DiagramTextItem(Gtk.DrawingArea, Presentation, DiagramTools):
    """
    Diagram text item.

    This item is used to display text on a diagram.
    """

    __gtype_name__ = 'DiagramTextItem'

