import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

#all the constants
SLEEP = 50/1000
TAILLE_PAQUET = 1400
N_CYCLE = 50
TAILLE_PAQUET_RECEPTION = TAILLE_PAQUET
IP_BROADCAST = "255.255.255.255"
IP_BALISE = "10.1.1.1"
IP_RUNNER = get_ip_address()
PORT_BROADCAST = 3000
PORT_RECEPTION = 3003
PORT_EMISSION = 3002


#all the functions
def launch_process(f, args = None):
    """
    Function that launch a process and return the process ID (pid).
    If the function launch a process, the function return himself the pid of the process.
    Else if the function launch a thread, the function return the PID of the thread.
    """
    def f_wrapper(q, *args):
        pid = os.getpid()
        q.put(pid)
        return f(*args)
    q = Queue()
    if args is None:
        p = Process(target
