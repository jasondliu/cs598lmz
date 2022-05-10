import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = ['Application']


class Application(_core.Application):
    """
    Application class.

    :param str title: The title of the application.
    :param str app_id: The application id.
    :param bool enable_high_dpi_scaling: Enable high DPI scaling.
    :param bool use_opengl: Use OpenGL.
    :param bool use_vulkan: Use Vulkan.
    :param bool use_metal: Use Metal.
    :param bool use_d3d11: Use Direct3D 11.
    :param bool use_software_rendering: Use software rendering.
    :param bool use_desktop_gl: Use desktop OpenGL.
    :param bool use_angle: Use ANGLE.
    :param bool use_software_rasterizer: Use software rasterizer.
    :param bool use_system_default_font: Use system default font.
    :param bool use_emoji: Use emoji.
    :param bool use
