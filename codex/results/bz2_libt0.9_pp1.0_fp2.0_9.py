import bz2
bz2.BZ2Compressor(compresslevel=9)

last_install_time = 0
last_uuid = None
uuid_re = re.compile(
    '^.*=.*\s(?P<uuid>[a-zA-Z0-9-]*)\s.*$', re.MULTILINE)
install_meta_re = re.compile(
    '^.*Installtime=(?P<installtime>\d+\Z)', re.MULTILINE)
savn_logs_re = re.compile(
    '^.*(?P<filename>savnlogs-\d+).*', re.MULTILINE)
GUID_LOG_FOLDER = '/etc/logrotate.d/guid/'
SAVN_LOG_FOLDER = '/opt/rbt/guid/logs/'
SAVN_LOG_LIST = '/opt/rbt/guid/config/log_list.conf'
logger = logging.getLogger(__name__)
logger.set
