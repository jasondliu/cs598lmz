import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

import rx.linq
import rx.subjects
import rx.disposables

from rx.disposables import Disposable
from rx.concurrency import immediate_scheduler
from rx.concurrency import new_thread_scheduler
from rx.internal import extensionmethod

@extensionmethod(rx.subjects.Subject)
def subscribe_on_ui(self, scheduler=None):
    scheduler = scheduler or new_thread_scheduler.NewThreadScheduler()
    def run(wnd, msg, data, result):
        def subscribe(observer):
            def action(state):
                observer.on_next(state)

            def handler(hWnd, message, wParam, lParam):
                if message != msg:
                    return
                state = data.state
                ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(state[0]), ctypes.py_object(Exception))

            Disposable.create(lambda: wnd.UnregisterClass(data.cl
