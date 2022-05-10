import weakref
import rx
import rx.operators as ops
from rx import disposable
from rx.internal import noop
from rx.core import typing
from rx.core.typing import Scheduler


def _add_ref(xs, r):
    def on_subscribe(observer, scheduler):
        def on_dispose():
            try:
                r.dispose()
            except Exception:  # pylint: disable=W0703
                observer.on_error(sys.exc_info()[1])
            else:
                return

        return disposable.create(on_dispose)

    return rx.pipe(xs, ops.tap(noop), ops.subscribe_on(scheduler),
                   ops.subscribe(on_subscribe=on_subscribe))


def _ref_count() -> typing.Callable[[Observable], Observable]:
    connectable_sources = weakref.WeakSet()

