import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 加入安全库中
import sys
sys.path.append('./safeLib')

# 加入自定义库中
import codeLib
import dbLib
import fileLib
import netLib

# 定义日志
log_path = fileLib.cwd(__file__)
# 日志路径
log_path = log_path + '/../logs/'
# 日志名称
log_name = log_path + 'qichacha.log'
# 日志格式
log_format = '%(levelname)s: %(asctime)s [%(threadName)s:%(thread)d]【%(name)s】 %(message)s'
# 设置日志格式
logging.basicConfig(

