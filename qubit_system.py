import numpy as np
import math as m


class Qubit_system:
    def __init__(self, n):
        self.n = n
        self.co = np.zeros(int(np.exp2(n)), dtype= complex) #coefficients of states;
        self.co[0] = 1 # assume that everythings go zero; 

    def gate(idx, matrix):
          pass
    
    def measure_all(self):
          print(self.co)
          prob_array = np.abs(self.co)*np.abs(self.co)
          print(prob_array)
          normalized = prob_array / np.sum(prob_array) # just for computing error..
          print(normalized)
          idx = np.random.choice(range(int(np.exp2(self.n))), p = normalized)
          self.co = self.co * 0
          self.co[idx] = 1
          return idx

if __name__ == "__main__":
        qusit = Qubit_system(5)
        print(qusit.measure_all())
        N = 15

