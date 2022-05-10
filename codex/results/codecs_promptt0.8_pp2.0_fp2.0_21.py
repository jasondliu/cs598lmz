import codecs
# Test codecs.register_error('xmlcharrefreplace2', xmlcharrefreplace2)

module_dir = os.path.dirname(os.path.abspath(__file__))

# Add module to sys.path if needed
if module_dir not in sys.path:
    sys.path.append(module_dir)

# Set up django configuration
project_dir = os.path.join(module_dir, 'opencontext_py')
sys.path.insert(0, project_dir)
# Django settings for opencontext_py
if os.path.isfile(os.path.join(project_dir, 'settings_local.py')):
    settings_module = 'settings_local'
else:
    settings_module = 'settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
# configure django logging
logging.config.dictConfig(settings.LOGGING)

from django.contrib.sites.models import Site
from django.core.cache import cache
from django.core.wsgi import get_ws
