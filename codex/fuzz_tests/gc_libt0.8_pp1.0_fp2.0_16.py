import gc, weakref

from cpy.ast import Scope, Module, Predicate, PredicateRef, Node
from cpy.mapper import Mapper
from cpy.util import cached, is_var, is_predicate


class Schema:
    def __init__(self, name, sort=None, logic_type='prob'):
        self.name = name
        self.sort = sort
        self.logic_type = logic_type
        self.predicates = {}

    def add_predicate(self, p):
        assert is_predicate(p)
        if p.name in self.predicates:
            raise KeyError('Predicate {} already exists in schema'.format(p))
        else:
            self.predicates[p.name] = p

    def __str__(self):
        s = self.name + ':\n'
        for pred_name in sorted(self.predicates.keys()):
            s += str(self.predicates[pred_name]) + '\n'
        return s.strip()


class Schemas:
    def __
