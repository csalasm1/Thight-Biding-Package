"""Scaffold module meant to be an interface between model.py and scipy solvers.

TODO:

Construct Solver class
Test it building Hamiltonian object and finding its ground state
"""
import numpy as np
import scipy.linalg as spla

import model    # our very own way of constructing Hamiltonians
import signals    # another homemade module


class Solver:

    def __init__(self, op, pulse or style):    # style: 'eq' or 'neq'
        """Initialize Solver object and connect it with model.py."""
        # check if op is of model.Hamiltonian type
        self.operator = objs

        if self.op.bc == 'obc':
            self.method = spla.eigh_tridiagonal
        else:
            self.method = spla.eigh

    def __str__(self):    # could also be called repr
        """Print out relevant info on Solver object."""

    def solve(self):
        """Invoke self.method to solve the thing."""

    def ground_state(self, ...):
        pass


def ground_state(sol):
    pass


if __name__ == "__main__":
    ham = model.Hamiltonian(...)
    sol = Solver(ham, ...)
    # flag = sol.solve()
    # if flag:
    #     print('Everything OK')
    # else:
    #     print('We are in trouble!')
    print(sol)
    pass    # Put tests here...
