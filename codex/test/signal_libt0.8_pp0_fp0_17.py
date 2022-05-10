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


