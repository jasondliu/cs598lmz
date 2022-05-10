import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def run_code(lines, verbose=False):
    """
    Run an infrared remote control code.

    >>> run_code(['on 0'])
    >>> run_code(['off 0'])
    >>> run_code(['set_volume -1'])
    >>> run_code(['set_volume 0'])
    >>> run_code(['set_volume 30'])
    """
    if verbose:
        print ('\n'.join(lines))
    global irsend
    global lircd_socket
    irsend = subprocess.Popen(['irsend', '-d', lircd_socket] + lines,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(0.2)
    irsend.terminate()


def is_on():
    """
    Check whether device is on.
    """
    global irsend
    if irsend and
