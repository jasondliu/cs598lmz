import socket
import sys
import time

import pytest

from pydispatch import dispatcher
from pydispatch.robustapply import robustApply
from pydispatch.robustapply import robustApplyCallback
from pydispatch.robustapply import robustApplySignal
from pydispatch.robustapply import robustApplySignalArgs
from pydispatch.robustapply import robustApplySignalKwargs
from pydispatch.robustapply import robustApplySignalBoth


class TestRobustApply:
    def test_callback(self):
        def callback(arg):
            return arg

        assert robustApplyCallback(callback, (1,)) == 1
        assert robustApplyCallback(callback, (1,), {}, None) == 1

    def test_callback_exception(self):
        def callback(arg):
            raise Exception

        assert robustApplyCallback(callback, (1,)) is None
        assert robustApplyCallback(callback, (1,), {}, None) is None

    def test_callback_exception_with_error_handler(self):
        def callback(arg
