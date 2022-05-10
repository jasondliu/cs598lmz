import weakref
from datetime import datetime
from typing import Callable, Dict, Optional, Union

from rx.core import Observable, typing
from rx.disposable import CompositeDisposable, SingleAssignmentDisposable
from rx.internal import noop, default_sub_comparer
from rx.internal.utils import is_future
from rx.subject import Subject

from . import operators as ops
from .observable import ConnectableObservable
from .subjects import AsyncSubject, BehaviorSubject, ReplaySubject
from .typing import SchedulerLike
from .window import WindowObservable
from .windowtime import WindowTimeObservable
from .windowtoggled import WindowToggleObservable
from .windowwhen import WindowWhenObservable
from .windowwithtime import WindowWithTimeObservable


def _publish_future_or(*args):
    return args[0] if len(args) == 1 else args


def _publish_future_and(*args):
    return args[-1] if len(args) == 1 else args


def _publish
