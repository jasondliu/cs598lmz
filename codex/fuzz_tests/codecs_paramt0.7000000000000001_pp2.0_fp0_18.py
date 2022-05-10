import codecs
codecs.register_error('strict', codecs.ignore_errors)
#from core import *
from core.routes import Routes
from core.utils import *
from core.config import *
from core.settings import *
from core.db import *
from core.file_handler import *
from core.template import *
from core.controller import *
from core.view import *
from core.model import *

#from core.framework import init_framework
#from core.utils import init_utils
#from core.config import init_config
#from core.db import init_db
#from core.file_handler import init_file_handler
#from core.template import init_template
#from core.controller import init_controller
#from core.view import init_view
#from core.model import init_model

#import core.framework
#import core.utils
#import core.config
#import core.db
#import core.file_handler
#import core.template
#import core.controller
#import core.view
#import core.model


#from core.routes import Routes
