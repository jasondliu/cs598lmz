import threading
threading.DEBUG = True
if __name__ == "__main__":
    import os, sys
    dirname, fname = os.path.split(os.path.abspath(os.path.dirname(__file__)))
    sys.path.append(dirname)
    activate_this='{}/venv/bin/activate_this.py'.format(dirname)
    exec(compile(open(activate_this, "rb").read(), activate_this, 'exec'), dict(__file__=activate_this))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    from django.core.handlers.wsgi import WSGIHandler
    application = WSGIHandler()
</code>
The script also contains some <code>exec</code>. May be it could also be the cause of the problem?
What can cause that <code>WSGIHandler</code> is not found, but Django successfully manages to display the main page?

