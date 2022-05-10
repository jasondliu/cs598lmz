import gc, weakref
from collections import defaultdict
import random
from asyncio import Future
from idact.detail.call_sync import call_sync


def _state_transitions_match(state: State,
                             expected: State) -> bool:
    return set(state.transitions.values()) == set(expected.transitions.values())


@attr.s(hash=True)
class State(object):
    """
    A state of the state machine.

    Designed to be used with attrs.

    :param str name: Name of the state.

    :param dict transitions: Map of transitions.

    """

    def __attrs_post_init__(self):
        self.transitions = attr.asdict(self)
        name = attr.fields_dict(self.__class__)['name']
        del self.transitions[name]

    @property
    def name(self) -> str:
        return attr.fields_dict(self.__class__)['name'].default

    def transition(self, id: str, state: str):
        """Sets
