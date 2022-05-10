import weakref

class State:
    """docstring for State"""
    def __init__(self, name):
        self.name = name
        self.transitions = []

    def add_transition(self, input, transition):
        self.transitions.append((input, transition))

    def __str__(self):
        return "State " + self.name

    def __repr__(self):
        return "State " + self.name

    def __eq__(self, other):
        if other is None:
            return False
        return self.name == other.name

    def clear(self):
        self.name = None
        self.transitions = None


class Transition:
    """docstring for Transition"""
    def __init__(self, name):
        self.name = name
        self.states = []

    def add_state(self, state):
        self.states.append(state)

    def __str__(self):
        return "Transition " + self.name

    def __repr__(self):
        return "Transition "
