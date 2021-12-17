"""Scaffold module meant to be an interface between model.py and scipy solvers.

TODO:

Construct Solver class
Test it building Hamiltonian object and finding its ground state
"""
import numpy as np
import scipy.linalg as spla
import sys

import model as model   # our very own way of constructing Hamiltonians
import signals    # another homemade module


class Solver:

    def __init__(self, op, pulse):    # style: 'eq' or 'neq' add 'no pulse' to signals? =>eq=>no style needed
        """Initialize Solver object and connect it with model.py."""
        # check if op is of model.Hamiltonian type
        if isinstance(op, model.Hamiltonian):
            self.op = op
        else:
            sys.exit("Object Hamiltonian is not class model")
        # check if pulse is of signals.Signals type
        if isinstance(pulse, signals.Signals):
            self.pulse = pulse
        else:
            sys.exit("Object Pulse is not class signals")

        if self.op.bc == 'obc':
            self.method = spla.eigh  #_tridiagonal  Prob(symmetric): Method needs off diagonal arguments, when complex are added, que get troubles.
        else:
            self.method = spla.eigh
        #print(str(self.method))

        
        self.solve =1 #How to fix this?
        self.grounde =0
        self.ground=0

    def __str__(self):    # could also be called repr
        """Print out relevant info on Solver object."""

    @property
    def solve(self):
        return self._energies
    
    @solve.setter
    def solve(self, pulse):
        print("solver setter going")
        """Invoke self.method to solve the thing."""
        self._energies = self.method(self.op.ham,eigvals_only = False)
        

    def ground_state(self):
        '''Assuming we don't take spin into account, we'll get only one ocupation e- for each space
        '''
        try:
            newN = int(self.op.length/2)
            self.total_E = np.sum(self.solve[0][0:newN])
            self.total_eigen = self.solve[1][0:newN]
        except NameError:
            newN = int((self.op.lenght-1)/2)
            self.total_E = np.sum(self.solve[0][0:newN])
            self.total_eigen = self.solve[1][0:newN]
        print("calculating ground state")
        return self.total_E,self.total_eigen               #wich k, because the eigenvectors should be related but i can't seem to find it when they loose symetry (if pulse).     

    @property
    def ground(self):
        return self._grounde
    
    @ground.setter
    def ground(self, pulse):
        print("ground setter going")
        """Return ground state energy and state."""
        self._grounde= self.ground_state()


if __name__ == "__main__":
    hop, ene = np.array((-1.,1.,2.)), [2., -2.,3.,1.]
    hami = model.Hamiltonian(ene=ene, hop=hop,bc ='obc')
    func, carrier, phase, time = 1., 2., -3,[0., 5.,2.]
    pulses = signals.Signals(func, carrier, phase, time)
    sol = Solver(hami,pulses)
    #print(sol.solve)
    print(sol.ground)
    # flag = sol.solve()
    # if flag:
    #     print('Everything OK')
    # else:
    #     print('We are in trouble!')
    #print(sol(),"\n")
    pass    # Put tests here...
