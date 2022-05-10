import weakref
from typing import Callable, Optional


class WindowManager(object):
    """
    Interacts with the window manager to get events about the window state.
    """

    def __init__(self, window: Window) -> None:
        self._window = weakref.ref(window)  # type: Optional[Window]

        self._window_event_handlers = {
            'configure_event': self._on_configure,
            'delete_event': self._on_delete,
        }

        self._fullscreen_event_handlers = {
            'key_press_event': self._on_key_press,
            'key_release_event': self._on_key_release,
            'motion_notify_event': self._on_motion,
            'button_press_event': self._on_button_press,
            'button_release_event': self._on_button_release,
            'scroll_event': self._on_scroll,
        }

    def manage(self) -> None:
        """
        Start monitoring the window state.
        """
