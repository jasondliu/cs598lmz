import signal
# Test signal.setitimer
def alarm(signum, stackframe):
    print("{0}: Ouch".format(signum))
signal.alarm(5)
signal.signal(signal.SIGALRM, alarm)
# 11.8 执行子进程
import subprocess
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))

# 11.9 测试可执行文件
import inspect
def test():
    return inspect.stack()[1]
def example():
    return test()
if __name__ == '__main__':
    print(example())

# 11.10 执行时间

# 11.11 打印重定向
import sys
saveout = sys.stdout
sys.stdout=open('out99.txt', 'a')
print('runoob')
sys.stdout.close()
sys.stdout
