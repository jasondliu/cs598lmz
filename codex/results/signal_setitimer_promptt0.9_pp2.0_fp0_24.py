import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

def time_out_handler(signum, frame):
    messagebox.showwarning('Notice', 'Time out')
    exit(0)
signal.signal(signal.SIGALRM, time_out_handler)
win = Tk()
win.title('超时检测')
while True:
    win.update()

# 下面这种做法会报错
# def alarm():
#     print('fun alarm()')
# signal.signal(signal.SIGALRM, alarm)
# signal.alarm(1)
# win = Tk()
# win.mainloop()

# messagebox.showinfo('❤', 'You are so beautiful')
# # 注意是先输出，后弹框，后退出
# print('end')
# exit(0
