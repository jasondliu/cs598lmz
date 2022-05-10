import weakref

_CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}
_LOG_LEVEL_MAPPING = {"DEBUG": logging.DEBUG, "INFO": logging.INFO, "WARNING": logging.WARNING, "ERROR": logging.ERROR, "CRITICAL": logging.CRITICAL}

class _Command(click.Command):
    def __init__(self, *args, **kwargs):
        click.Command.__init__(self, *args, **kwargs)
        self._gt_manager = None
        self._gt_command_class = None

    def _gt_init(self, gt_manager, gt_command_class):
        self._gt_manager = weakref.proxy(gt_manager)
        self._gt_command_class = gt_command_class

    def _gt_get_manager(self):
        return self._gt_manager

    def invoke(self, ctx):
        command = self._gt_command_class(ctx)
        return command._invoke(ctx)


class Griddata
