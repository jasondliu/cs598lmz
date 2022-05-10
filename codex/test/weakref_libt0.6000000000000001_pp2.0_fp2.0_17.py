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

