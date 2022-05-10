import _struct
import os

# these are the default values for the params in the 
# VMD movie maker tcl script
DFLT_WIDTH = 320
DFLT_HEIGHT = 240
DFLT_FPS = 15
DFLT_OUTNAME = "movie"
DFLT_FFMPEG = "ffmpeg"

class VMDMovieMaker:
    """
    This class is designed to make movies in VMD using the build-in movie
    making capabilities in VMD.

    The tcls for this class were obtained from the VMD mailing list as
    posted by John Stone on Thu, 14 Aug 2008 10:40:04 -0500:

    http://www.ks.uiuc.edu/Research/vmd/mailing_list/vmd-l/35061.html

    The top of the tcl file should look like the following:

    # VMD movie maker script
    # John Stone
    # Thu, 14 Aug 2008
    #
    # Fixed by Hans Fangohr (13-Dec-2010) to allow for HD image
    # recording, and any other resolution
