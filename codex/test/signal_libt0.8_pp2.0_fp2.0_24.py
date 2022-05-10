import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) # enable CTRL+C

#y = np.load('signalData.npy')

def update(val):

    f0 = sfreq.val
    Q = sQ.val
    A = sA.val
    f1 = sf1.val
    #print(f0)
    if f0 > 5000:
        f1 = f0
    #data,t = update_line(data,t,f0,Q,A,f1)
    lines.set_ydata(gen_signal(f0,Q,A,f1))
    fig.canvas.draw_idle()

def update_line(data,t,f0,Q,A,f1):
    data = gen_signal(f0,Q,A,f1)
    return data,t

