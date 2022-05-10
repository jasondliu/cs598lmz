import select
import sys
import time

from . import _common
from . import _constants
from . import _util
from . import _video_opt
from . import _video_opt_parser
from . import _video_renderer
from . import _video_renderer_gtk
from . import _video_renderer_pygame


def main(
        video_filename,
        video_renderer_class=_video_renderer_gtk.VideoRendererGtk,
        verbose=False,
        ):
    """Main loop for the video player.

    Args:
        video_filename: Filename of the video to play.
        video_renderer_class: Class to use for rendering the video.
        verbose: If True, print extra information.

    Returns:
        Exit code.
    """
    # Parse command line options.
    parser = _video_opt_parser.VideoOptParser()
    video_opt = _video_opt_parser.VideoOpt(
        video_filename=video_filename,
        video_renderer_class=video_rend
