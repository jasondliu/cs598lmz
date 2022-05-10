import types
types.ClassType = type

def _print(output):
    """
    Prints a message, and ensures that the output is immediately flushed,
    so that AJAX requests don't have to wait for a full buffer to be flushed.
    """
    print output
    sys.stdout.flush()

def _exception_handler(exception):
    """
    Returns a 500 error with the result of calling unicode() on the
    exception instance.
    """
    if settings.DEBUG:
        if isinstance(exception, Http404):
            # Call the regular Django 404 error handler,
            # so that the 404 HTTP status code gets set.
            django.views.defaults.page_not_found(
                django.core.handlers.wsgi.WSGIRequest({'PATH_INFO': '/'}))
        else:
            # Call the regular Django 500 error handler,
            # so that the 500 HTTP status code gets set.
            django.views.defaults.server_error(
                django.core.handlers.wsgi.WSGIRequest({'PATH_INFO
