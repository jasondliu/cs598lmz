import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('Falmer')

opts = [
    cfg.StrOpt('name', default=socket.gethostname()),
    cfg.BoolOpt('rest_api', default=True),
    cfg.IntOpt('port', default=8181),
]
CONF = cfg.CONF
CONF.register_cli_opts(opts)
logger = logging.getLogger('falmer')
LOG_FORMAT = '[%(asctime)s][PID:%(process)d][%(levelname)s] %(message)s'
logging.basicConfig(format="[%(asctime)s][PID:%(process)d][%(levelname)s] %(message)s",
                    level=logging.INFO)

logging.addLevelName(logging.DEBUG, "\033[1;34m%s\033[1;0m" % logging.getLevelName(logging.DEBUG))
logging.addLevelName(logging.INFO
