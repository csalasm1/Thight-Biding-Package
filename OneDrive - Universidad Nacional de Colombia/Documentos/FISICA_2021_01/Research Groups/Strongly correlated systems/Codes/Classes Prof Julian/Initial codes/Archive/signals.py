"""Scaffold for signals module. Allows to choose light profile.

TODO:

Check signals module from qiskit's quantum dynamics
Everything
Need to connect with model and solver


QUESTION:
I'm thinking Signals should work just like signals qiskit, and the envelops could be on the utilities program.
Then, depending on the chosen signal, it should go to model and change the hamiltonian, right?
If not, should this create a light hamiltonian and make site matrix multiplication for off diag inside solver?
I believe there would be problems doing that. 
"""

import numpy as np
# import something from scipy?
from typing import List, Callable, Union, Optional, Tuple 
import collections
import matplotlib as plt

class Signals:

    def __init__(
        self,
        envelope: Union[Callable, complex, float, int, np.ndarray], 
        carrier_freq: Union[float, List, np.ndarray] = 0.0, #list to get \nu(t)?
        phase: Union[float, List, np.ndarray] = 0.0, #\phi(t) wouldn't make sense. Would do it as [float,collection.abc.Iterable]
        time: Union[collections.abc.Iterable] = 0.0, #Thinking np.array((t0,tf,Deltat))
        name: Optional[str] = None,
    ):
        self._name = name
        self._is_constant = False
        time = [int(i) for i in time]
        self.t = np.linspace(time[0],time[1],time[2])
        #self.fpulse =1
        #self.carrier_freq = 2
        self.carrier_freq = 1
        self.phase = 3
        
        if isinstance(envelope,collections.abc.Iterable): #is this redundant given instance variable def?
            envelope = np.array(envelope, dtype=complex)
        elif isinstance(envelope, Callable):
##            self._envelope = lambda t: np.array(envelope(t) ,dtype=complex)
            self._envelope = np.array(envelope(self.t) ,dtype=complex)
        else:
            envelope = np.array(complex(envelope))
##            self.envelope = lambda t: envelope*np.ones_like(t)# lambda t useful because is not yet specified t is np.ndarray
            self.envelope = envelope*np.ones_like(self.t)

    @property
    def times(self):
        """Caller for time interval of the signal"""
        return self._times
    @times.setter
    def times(self,time):
        """"Time setter of the signal (duration)"""
        if isinstance(time,collections.abc.Iterable):
            time = list(time)
        self._times = np.linspace(time[0],time[1],time[2])
        
    @property
    def carrier_freq(self):
        """The carrier frequency of the signal."""
        return self._carrier_freq

    @carrier_freq.setter
    def carrier_freq(self, carrier_freq: Union[float, list, np.ndarray]):
        """Carrier frequency setter. List handling is to support subclasses storing a
        list of frequencies. I was thinking it might be useful instead a time dependent frecuency?"""
        if isinstance(carrier_freq,collections.abc.Iterable):
            carrier_freq = np.array(carrier_freq,dtype=complex)
        self._carrier_freq = carrier_freq
        self._carrier_arg = 1j * 2 * np.pi * self._carrier_freq

    @property
    def phase(self):
        """The phase of the signal."""
        return self._phase

    @phase.setter
    def phase(self, phase: Union[float, list, np.ndarray]):
        """Phase setter. List handling is to support subclasses storing a
        list of phases."""
        print("is phase workin?")
        if type(phase) == list:
            phase = np.array(phase,dtype=complex)#they use Array class, and phase(t) doesn't seem logical
        self._phase = phase
        self._phase_arg = 1j * self._phase


##    @property
##    def fpulse(self):
##        print("getter fpulse")
##        return self._fpulse

    #@fpulse.setter
    def fpulse(self):
        print("executing func setter")
        self.resultf = self.envelope * np.exp(self.carrier_arg+self.phase_arg)
        self._fpulse = np.real(self.result)
        return self._fpulse
    
    def __str__(self):
        strg = "Chosen otential:\n"
        strg += "Name: " + str(self._name) + ", "
        strg += "Envelope: " + str(self.envelope) + "\n"
        strg += "freq:\n" + str(self.carrier_freq) + "\n"
        strg += "Phase:\n" + str(self.phase)

    def __call__(self, full=True):
        if full:
            return self.fpulse() #got very confused here
        #return self.enes, self.hops

    @property
    def name(self):#-> str
        """Return the name of the signal."""
        return self._name

if __name__ == "__main__":
    func, carrier, phase, time = 1., 2., -3,[0., 5.,2.]
    sign = Signals(func, carrier, phase, time)

    print(sign.times, '\n')
    #print(sign.__dict__)
    #print(Signals.__dict__)
    
