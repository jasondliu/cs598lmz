import types
types.ModuleType
sys.path.append('/Users/paul/PROJECTS/WEBSITES/OBDKTEST/PYTHONDJANGO/OBDKMAIN/OBDKMAIN')
sys.path.append('')
os.environ['OBDKDB'] = 'obdkdb'
os.environ['OBDKCELERY'] = 'obdkcelery'

os.environ['OBDKDBUSERNAME'] = 'obdkdbuser'
os.environ['OBDKDBPASSWORD'] = 'obdkdbpassword'
os.environ['OBDKDBHOST'] = 'localhost'
os.environ['OBDKDBPORT'] = '5432'


os.environ['OBDKREDISHOST'] = 'localhost'
os.environ['OBDKREDISPORT'] = '6379'
os.environ['OBDKREDISDBF'] = '0'
os.environ['OBDKADMINEMAIL'] = 'redacted@gmail.com'
os.environ['OBDKAPPNAME'] = 'OBDK'
