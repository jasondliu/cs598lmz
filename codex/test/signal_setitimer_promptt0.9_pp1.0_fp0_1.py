import signal
# Test signal.setitimer for old POSIX systems lacking RLIMIT_CPU
signal.setitimer(signal.ITIMER_REAL, 0, 1)

def dump_coverage() :
    """Sets and dumps the code coverage data.  This is called from the
    signal handler."""
    global _cover_code, _cov_path, _cov_chunks

    # Find a random filename
    while True :
        name = os.path.join("bratwurst_coverage/" + _app_name,
                            ("%04x.txt" % random.randrange(65536)))
        try :
            fd = open(name, "xb")
        except FileNotFoundError :
            # Make the directory
            os.makedirs(os.path.dirname(name))
            continue
        except OSError as e :
            if e.errno != 17 : raise
            # The file already exists; try again
            continue
        fd.close()
        break

    # The coverage information is measured in chunks of 262144 instructions.
    # This gives us
