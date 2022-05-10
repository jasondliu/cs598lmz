from types import FunctionType
list(FunctionType(lambda: False))
int(False)
float(0)
bool(bool(False))
type(FunctionType)
~0xFFFFFFFF
~~0xFFFFFFFF
~~~0xFFFFFFFF

# 24. 缺省参数的“惰性赋值”
arg = arg or default_value


# 25. 初始化列表 - list-initialization
import subprocess
import shlex
def popen(cmd, *args, **kwargs):
    if isinstance(cmd, (list, tuple)):
        cmd = subprocess.list2cmdline(cmd)
    cmd = shlex.split(cmd)
    return subprocess.Popen(cmd, *args, **kwargs)
# calling:
popen(['ls', '-l', '/dev/null'])
popen('|'.join(['ls', '-l', '/dev/null']))


# 26. 解析器父子句绑定 - parser descendent binding
