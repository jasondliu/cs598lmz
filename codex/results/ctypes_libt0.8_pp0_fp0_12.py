import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("DB_backup")

# 设置打印到文件
print ('This output will be written to a file')
sys.stdout = open('output.txt', 'w')

env_dist = os.environ
env_dist = dict([(env_key.upper(), env_dist[env_key]) for env_key in env_dist])

# 获取数据库连接参数
HOSTNAME = env_dist['DB_IP']
USERNAME = env_dist['DB_USERNAME']
PASSWORD = env_dist['DB_PASSWORD']
DATABASE = env_dist['DB_NAME']
PORT     = env_dist['DB_PORT']
filename = './' + DATABASE + '.sql'

# 获取备份文件存放路径
backup_dir = env_dist['BACKUP_DIR']

#
