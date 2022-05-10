import types
# Test types.FunctionType in function_type.py
#
# (C) Frank-Rene Schaefer
#______________________________________________________________________________
import sys
import unittest
sys.path.insert(0, ".")

from   quex.engine.misc.interval_handling import NumberSet, Interval
from   quex.output.core.state.transition_map import TransitionMap
from   quex.engine.state_machine.core        import StateMachine
from   quex.engine.state_machine.algorithm.beautifier import do as beautifier
from   quex.engine.state_machine.algorithm.beautifier import __drop_epsilon_transitions
from   quex.engine.state_machine.check.identity    import are_identical_sm
from   quex.engine.state_machine.index import map_state_index_to_state_key
import quex.blackboard as blackboard

if "--hwut-info" in sys.argv:
    print "State Machine: Epsilon Transition Removal (drop_epsilon_transitions)"
    sys.exit(0)

