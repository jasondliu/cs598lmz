import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# 解决导入路径问题
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from config import *
from core import *

def main():
    '''
    ftp服务器启动
    :return:
    '''
    # 实例化对象
    ftp_server = FTPServer(settings)
    # 启动服务端
    ftp_server.start()

if __name__ == '__main__':
    main()
