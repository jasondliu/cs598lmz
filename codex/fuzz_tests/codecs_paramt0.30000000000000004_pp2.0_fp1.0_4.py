import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Import the project config
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../../config'))
import config_web

# Import the project libs
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../lib'))
import logger
import utils

# Import the project models
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../models'))
import db_web

# Import the project libs
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../lib'))
import logger
import utils

# Import the project libs
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../lib/tasks'))
import task_web

# Import the project libs
sys.path.append
