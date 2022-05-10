import mmap
import os
import random
import re
import sys
import time

# 将当前目录设置为工作目录，则可以不用写全路径
os.chdir("C:\\Users\\Administrator\\Desktop\\testPython")

###################################################################################################
####################### 问题：读取文件类型及大小，解码编码；字符串处理；文件分割；日志级别；单元测试 #############################

'''
1、读取文件类型及大小，解码编码；
    从sys模块中用exists函数
