import signal
signal.signal(signal.SIGINT, sigint)

def sigusr1(signum, frame):
    global response_time
    global request_time
    print("{:03.2f}".format(response_time / request_time))

def sigusr2(signum, frame):
    global max_request_time
    print("{:03.2f}".format(max_request_time))

signal.signal(signal.SIGUSR1, sigusr1)
signal.signal(signal.SIGUSR2, sigusr2)

def loop_and_work(sock):
    global response_time
    global health_mark
    global max_request_time
    global request_time
    global no_response_time
    global response_msg
    global health_state
