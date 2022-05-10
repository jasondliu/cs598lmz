import threading
threading.stack_size(2**27)

import pycosat

class SATSolver(object):

    def __init__(self, num_variables):
        self.num_variables = num_variables
        
    def add_clause(self, clause):
        self.clauses.append(clause)
        
    def all_sat(self):
        assert False, "all_sat() not implemented"
        
    def solve(self):
        assert False, "solve() not implemented"
        
    def get_model(self):
        assert False, "get_model() not implemented"
        
    def get_num_variables(self):
        return self.num_variables
        
    def get_num_clauses(self):
        return len(self.clauses)
    
