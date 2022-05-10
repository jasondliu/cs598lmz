import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class STBLocale(Action):
    """
    This action is used to change locale when a translation is missing
    """
    def run(self, locale=None, **kwargs):
        if locale:
            if locale == 'en':
                translation.activate('')
            else:
                translation.activate(locale)
            request.session[translation.LANGUAGE_SESSION_KEY] = locale


class STBFormView(FormView):
    """
    Base class for a form, which includes some handy stuff for handling a
    form submission.
    'action' should be set to one of ('save', 'reset')
    'next' should be set to a URL, which will be the next page the user is taken to
    'success_message' can be optionally set to a message to display on successful submission
    'form_class' should be set to a django form class
    'form_kwargs' can be optionally set to any additional arguments to instantiate the form with
    'context_
