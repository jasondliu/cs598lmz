import select
# Test select.select([sys.stdin], [], [], 0) #
# Test select.select([stdin], [], [], 0)  # 当没有输入的时候，会一直卡在这个位置； 当输入的时候，允许本次输出； 但是，这个是全局的监测的
# 由上述可以知道： 可以一直监测输入的监听
# Test select.select([sys.stdout], [], [], 0) # 输出
# Test select.select([sys.stderr], [], [], 0) # 错误
# Test select.select([stdout], [], [], 0) # 输出
# Test select.select([stderr
