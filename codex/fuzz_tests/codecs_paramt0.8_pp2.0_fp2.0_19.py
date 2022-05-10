import codecs
codecs.register_error('txt_replace', txt_replace)


import errno
from io import StringIO
from io import BytesIO
from logging.handlers import TimedRotatingFileHandler
from time import time

from univention.lib.udm import NoObject
from univention.lib.udm import LDAP_MOD_DELETE
from univention.management.console.config import ucr
from univention.management.console.log import MODULE
from univention.management.console.modules.diagnostic import Warning
from univention.management.console.modules import UMC_Error
from univention.management.console.modules.diagnostic import util
from univention.management.console.modules.diagnostic import util_ldap
from univention.management.console.modules.diagnostic import util_umc
from univention.management.console.modules.diagnostic import util_umc_ldap
from univention.management.console.modules.diagnostic import util_simpleldap
from univention.management.console.modules.diagnostic import util_usershare
from un
