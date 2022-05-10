fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# 用于检查程序的标准输入、输出
# https://docs.python.org/3/library/io.html#io.StringIO
# http://python.jobbole.com/81233/
# https://stackoverflow.com/questions/10742914/what-is-the-difference-between-python-stringio-and-io-stringio
# https://stackoverflow.com/questions/16810177/python-io-stringio-vs-stringio-stringio
# https://stackoverflow.com/questions/10742914/what-is-the-difference-between-python-stringio-and-io-stringio
# https://stackoverflow.com/questions/16810177/python-io-stringio-vs-stringio-stringio
# https://stackoverflow.com/questions/10742914/what-is-the-difference-between-python-stringio-and-io
