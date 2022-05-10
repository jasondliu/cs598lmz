import weakref

from pytestqt.qtbot import QtBot


class QTestHelper(object):
    """
    Helper class to provide a more convenient interface to qtest methods.

    This class is a thin wrapper around QTest that provides a more convenient
    interface to the methods of QTest.
    """

    def __init__(self, qtbot):
        self.qtbot = qtbot

    def key_click(self, widget, key, modifier=None, delay=-1):
        """
        Simulates a key click on a widget.

        :param widget: Widget to click on
        :type widget: QWidget
        :param key: Key to click
        :type key: QtCore.Qt.Key
        :param modifier: Modifier to use
        :type modifier: QtCore.Qt.KeyboardModifier
        :param delay: Delay between press and release events
        :type delay: int
        """
        if modifier is None:
            QTest.keyClick(widget, key, delay=delay)
        else:
            QTest.keyClick(widget, key,
