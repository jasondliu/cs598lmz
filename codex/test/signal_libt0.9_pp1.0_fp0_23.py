import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

## constants
from cdb import constants

##
from cdb import cdb_web_service
from cdb.cdb_web_service import app

from cdb.platform.mom.post_actions import SoftwareInstall, SoftwareUninstall, SetHost, SetLaser
from cdb.platform.mom.post_actions import FreecdbwebService
from cdb.common.exceptions import CdbPermanentError
from cdb.common.exceptions import CdbTemporaryError

from cdb.common.db.api import init_connection
from cdb.platform.mom import mom_utils
from cdb.platform.mom.mom_utils import getPostActionHandlerInstance

@app.route(constants.MOM_SERVICE_SOFTWARE_INSTALL, constants.MOM_SERVICE_API_VERSION)
def momSoftwareInstall():
    parms = request.get_json(force=True)
