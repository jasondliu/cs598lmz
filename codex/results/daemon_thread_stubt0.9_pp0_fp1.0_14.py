import sys, threading

def run():
    from django.core.management import execute_manager
    try:
        import settings # Assumed to be in the same directory.
    except ImportError:
        import sys
        sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
        sys.exit(1)

    if not settings.DEBUG and not settings.SESSION_COOKIE_SECURE:
        print >> sys.stderr, "ERROR: You have not set SESSION_COOKIE_SECURE = True in your settings file.  This is required for https session management to work properly."
        print >> sys.stderr, "(settings file is %s)" % settings.SETTINGS_MODULE
        sys.exit(1)

    execute_manager(settings)


def main(argv):
    # Start the server
