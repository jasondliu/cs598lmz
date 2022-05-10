import signal
signal.signal(signal.SIGINT, terminate_handler)


# Create a new process to execute a command
def execute_cmd(cmd):
    # Create a subprocess
    process = subprocess.Popen(cmd, shell=True)
    # Wait for subprocess to finish and get return code
    while True:
        nextline = process.stdout.readline()
        if nextline == '' and process.poll() is not None:
            break
        sys.stdout.write(nextline)
        sys.stdout.flush()

    output = process.communicate()[0]
    exit_code = process.returncode

    if (exit_code == 0):
        return output
    else:
        raise ProcessException(cmd, exit_code, output)


# Create a new process to execute a command
def execute_cmd_bg(cmd):
    # Create a subprocess
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    return process


#
