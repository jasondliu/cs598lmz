import signal
# Test signal.setitimer()
# setitimer(which, seconds, interval = 0)
# which = ITIMER_REAL, ITIMER_VIRTUAL, ITIMER_PROF
# 测试结果：
# 1. ITIMER_REAL, sec=3, interval=0.5,  前两次调用间隔大约3-3.5s, 后续调用间隔0.5s
# 2. ITIMER_VIRTUAL, sec=5, interval=2, 前两次调用间隔大约5-5.5s, 后续调用间隔2s
# 3. ITIMER_PROF, sec=4, interval=1,    后两次调用间隔2s
######

# def test_setitimer():
#     def handler(signum, frame):
#        
