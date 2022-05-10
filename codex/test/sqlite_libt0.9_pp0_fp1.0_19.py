import ctypes
import ctypes.util
import threading
import sqlite3

# 正常的
AUTHID_0    = 0
# 账户被用于已经连接的公共登录
AUTHID_1    = 1
# 账户被禁用
AUTHID_2    = 2
# 连接超时
AUTHID_3    = 3
# 未知错误,可能是账户文件错误
AUTHID_4    = 4
# 账户被禁止登录
AUTHID_5    = 5
# 账户数目超过最大值
AUTHID_6    = 6

# 用户登录成功,准备连接语音服务器
