import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

string='192.168.1.1'
t=a.login(string, 22)
if t[0] ==1:
    print('Password is ',t[1])
elif t[0] == 0 :
    print('illegal ip or port')
else:
    print('stuf occured')
t1=a.get_portscan()
if t1 == 'TCP_Scan':
    print('TCP_SCAN Trigerred')
elif t1 == 'UDP_Scan':
    print('UDP_SCAN Trigerred')
else :
    print('nothing happened')
t2=a.gen_random_string(2)
