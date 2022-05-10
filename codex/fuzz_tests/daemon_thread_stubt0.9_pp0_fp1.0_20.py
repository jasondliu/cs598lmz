import sys, threading

def run():
    try:
        run_once()
    except KeyboardInterrupt:
        pass
    except:
        exc = traceback.format_exc()
        print "Unhandled error. Sending email."
        send_error_mail(exc)
        print "Done."
        sys.exit(1)

    print "Daily job done. Sleeping..."
    try:
        timer = threading.Timer(86400, run)
        timer.start()
    except:
        exc = traceback.format_exc()
        print "Unable to set up timer. Sending email."
        send_error_mail(exc)
        print "Done."
        sys.exit(1)

if __name__ == "__main__":
    run()
