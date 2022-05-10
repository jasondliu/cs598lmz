import selector_utils
import render_utils
import logger
from render_utils import RENDER_NODE_TYPE, RENDER_MODE_NAMES

__author__ = 'Sebastian Bach'
__email__ = 'sebastian.bach@gmail.com'
__version__ = '0.2.0'

logger = logger.getLogger('AN:main')

#try to get the default Renderman path.
AN_PATH = os.path.dirname(__file__)
RENDMAN_PATH = cmds.getenv('RMANFB')
if not RENDMAN_PATH:
	RENDMAN_PATH = os.path.join(os.getenv('MAYA_APP_DIR'),
	                            'mentalray', 'shaders')
	if not os.path.exists(RENDMAN_PATH):
		RENDMAN_PATH = str()

#dynamic reloading of Renderman shaders
#for interactive development
DO_RELOAD = True


###############################################################################
# Control the assetNumberMaya UI
########################################################################
