import weakref

class TranscriptionServices():
    """Translates the text to a specific output format"""
    __shared_state = {}
    __available_services = {}

    class Service(object):
        """A specific service for transcription"""
        def __init__(self, input_format, output_format, method):
            self._method = method
            self._input_format = input_format
            self._output_format = output_format

        @property
        def input(self):
            """Return the service input format"""
            return self._input_format

        @property
        def output(self):
            """Return the service output format"""
            return self._output_format

        def __call__(self, text_to_translate):
            """Return the transcribed text"""
            return self._method(text_to_translate)

    def __init__(self):
        self.__dict__ = self.__shared_state

    def register(self, input_format, output_format, method):
        """Register an method to execute the service"""
        svc = self.Service
