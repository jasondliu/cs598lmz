fn = lambda: None
# Test fn.__code__.co_filename == '<stdin>'
# fn.__code__.co_filename == ''
##
if not os.environ.get('WEBPY_ENV'):
    os.environ['WEBPY_ENV'] = 'development'
    os.environ['WEBPY_ENV_AUTO_RELOAD'] = 'true'
##
if not os.environ.get('WEBPY_DATABASE_URI'):
    os.environ['WEBPY_DATABASE_URI'] = 'sqlite://data/database.sqlite'
##
from zipfile import ZipFile
import glob
def auto_load_from_zip():
    """
    从zip文件导入要加载的.py文件
    """
    _path = os.path.realpath(os.environ['WEBPY_APP_ROOT_PATH'])
    _z = glob.glob(os.path.join(_path, '*.zip'))
    #
    _r
