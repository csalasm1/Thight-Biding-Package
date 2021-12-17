"""Construct tight-binding Hamiltonians with open boundary conditions.

TODO:

Done // Handle pbc's
Done //(I think): Check if long < 3
Done // Check for nonempty arrays?
Partially with troubles // Make H (now ham) property? Read about @property in python.org or similar
"""
import numpy as np
import collections
import sys

class Hamiltonian:

    def __init__(self, long=None, ene=None, hop=None, bc='obc'):
        if long is not None and (type(hop) == float and type(ene) == float):
            # print('here')
            self.enes = np.array([ene] * long)
            self.hops = np.array([hop] * (long - 1))
        elif isinstance(hop,collections.abc.Iterable)and isinstance(ene,collections.abc.Iterable):# type(hop) in (list, tuple) and type(ene) in (list, tuple):
            #could also use Union from typing
            # print('there')
            self.enes = np.array(ene)
            self.hops = np.array(hop)
        else:
            sys.exit("Way of constructing Hamiltonian not supported")
            #raise ValueError("Way of constructing Hamiltonian not supported")


        self.bc, self.length = bc, len(self.enes)

        if len(self.enes) in (2,):
            self.bc = "obc"

        self.ham = 1 #Just because I don't know if variables should go inside ham


    def __str__(self):    # could also be called repr
        strg = "Hamiltonian:\n"
        strg += "L: " + str(len(self.enes)) + ", "
        strg += "BC: " + str(self.bc) + "\n"
        strg += "Energies:\n" + str(self.enes) + "\n"
        strg += "Hoppings:\n" + str(self.hops)
        return strg

##    def __call__(self, full=True):
##        if full:
##            return self._ham #got very confused here
##        return self.enes, self.hops
    @property
    def ham(self):
        print("getter returning")
        return self._ham
    
    @ham.setter
    def ham(self,val):
        print("setter going")
        self._ham = np.diag(self.enes)
        self._ham += np.diag(self.hops, 1) + np.diag(self.hops, -1)

        if self.bc == 'pbc':
           #self.hops = np.append(self.hops,self.hops[0])
           self._ham[0][len(self.hops)] += self.hops[0]
           self._ham[len(self.hops)][0] += self.hops[0]
        else:
            pass

    #ham = property(fget=get_ham,fset=set_ham)

if __name__ == "__main__": #Recordando que la idea es que al ser llamado como modulo no va a imprimir.
##    ell, hop, ene = 3, -1., 0.
##    ham = Hamiltonian(long=ell, ene=ene, hop=hop)
##    #print(ham, '\n')

    hop, ene = np.array((-1.,2.)), [2., -2.,3.1]
    hami = Hamiltonian(ene=ene, hop=hop,bc ='obc')
    #print(ham.__dict__)
    #ham.H
    #print(hami(), '\n') #() para la función call
    #print(Hamiltonian.__dict__)

    aloha = hami.ham*2
    print(aloha)

##    hop, ene = np.random.randint(-2, 0, 4), np.random.randint(-2, 3, 5)
##    ham = Hamiltonian(ene=ene, hop=hop)
##    #print(ham)
