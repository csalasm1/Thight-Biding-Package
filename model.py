"""Construct tight-binding Hamiltonians with open boundary conditions.

TODO:

Handle pbc's
Check if long < 3
Check for nonempty arrays?
Make H property? Read about @property in python.org or similar
"""
import numpy as np


class Hamiltonian:

    def __init__(self, long=None, ene=None, hop=None, bc='obc'):
        if long is not None and (type(hop) == float and type(ene) == float):
            # print('here')
            self.enes = np.array([ene] * long)
            self.hops = np.array([hop] * (long - 1))
        else:    # type(hop) in (list, tuple) and type(ene) in (list, tuple):
            # print('there')
            self.enes = np.array(ene)
            self.hops = np.array(hop)
        # else:
        #     print("Way of constructing Hamiltonian not supported")
        #     exit()

        self.bc, self.length = bc, len(self.enes)

        self.ham = np.diag(self.enes)
        self.ham += np.diag(self.hops, 1) + np.diag(self.hops, -1)
        # print(self.ham)

    def __str__(self):    # could also be called repr
        strg = "Hamiltonian:\n"
        strg += "L: " + str(len(self.enes)) + ", "
        strg += "BC: " + str(self.bc) + "\n"
        strg += "Energies:\n" + str(self.enes) + "\n"
        strg += "Hoppings:\n" + str(self.hops)
        return strg

    def __call__(self, full=True):
        if full:
            return self.ham
        return self.enes, self.hops

    def H(self):
        return self.ham


if __name__ == "__main__":
    ell, hop, ene = 3, -1., 0.
    ham = Hamiltonian(long=ell, ene=ene, hop=hop)
    print(ham, '\n')

    hop, ene = (-1., -2., -1.), [1., -1., 1., -1.]
    ham = Hamiltonian(ene=ene, hop=hop)
    print(ham)
    print(ham(), '\n')

    hop, ene = np.random.randint(-2, 0, 4), np.random.randint(-2, 3, 5)
    ham = Hamiltonian(ene=ene, hop=hop)
    print(ham)
