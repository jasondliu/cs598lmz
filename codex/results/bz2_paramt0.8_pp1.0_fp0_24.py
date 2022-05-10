from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2text)

# 使用压缩数据
import bz2
bz2.decompress(bz2text)

import subprocess 
pro = subprocess.Popen(['echo', '"to stdout"'], stdout=subprocess.PIPE)
pro.communicate()

# 可以以python脚本的方式调用系统命令
# 通过check_output()调用系统命令，并把它的输出保存到变量中，而不是屏幕上打印出来
# 可以用管道符来连接多个命令
# 子程序会把输出打印到屏
