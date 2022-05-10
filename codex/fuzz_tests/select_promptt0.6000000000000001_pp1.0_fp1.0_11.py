import select
# Test select.select()

def stdin_ready(timeout):
    """
    Test whether STDIN is ready to read within a timeout.
    """
    return select.select([sys.stdin], [], [], timeout) == ([sys.stdin], [], [])

def get_input(prompt, timeout):
    """
    Prompt the user for input within a timeout.
    """
    start_time = time.time()
    sys.stdout.write(prompt)
    sys.stdout.flush()
    input = ''
    while True:
        if stdin_ready(timeout):
            input = sys.stdin.readline()
            break
        else:
            sys.stdout.write('.')
            sys.stdout.flush()
            timeout = timeout - (time.time() - start_time)
            if timeout &lt;= 0:
                break
    return input

print get_input('&gt; ', 3)
</code>

