import weakref
from warnings import warn
from .graphics_container import GraphicsContainer
from .graphics_frame import GraphicsFrame
from .Text import Text

from . import labels
from . import shared_subjects
from . import subjects
from . import subjects_base
from . import subjects_factory

from .geometry import Coordinate
from .geometry import Point
from .geometry import Scalar
from .support_preferences import color_preferences


class TextFrame(GraphicsFrame):

    def __init__(self, **settings):
        super().__init__(**settings)


class TextContainer(GraphicsContainer):

    ### CLASS VARIABLES ###

    __documentation_section__ = "Containers"

    __slots__ = (
        "_deactivate_auto_position",
        "_label",
        "_root_container",
        "_text_settings",
        "_x_offset",
        "_y_offset",
    )

    _ignored_graphic_delegate_slots = (
        "_height",
        "_width",
    )

    ### INIT
