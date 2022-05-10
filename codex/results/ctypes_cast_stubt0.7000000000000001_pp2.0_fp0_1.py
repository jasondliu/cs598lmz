import ctypes
ctypes.cast(log_file, ctypes.py_object).value = file

# 日志输出
log4cxx.Logger.getLogger("").info("hello world")

# 关闭文件
file.close()

"""
"""
import log4cxx

# 配置文件
log4cxx.PropertyConfigurator.configure("conf/log4j.properties")

# 日志输出
log4cxx.Logger.getLogger("").info("hello world")
"""
"""
import log4cxx

# 创建日志对象
logger = log4cxx.Logger.getLogger("")

# 创建formatter
formatter = log4cxx.PatternLayout("%d{HH:mm:ss} %-5p %c{1}:%L - %m%n")

# 设置handler
handler = log4cxx.FileApp
